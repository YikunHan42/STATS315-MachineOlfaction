from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def fetch_lcss_data(cid):
    # URL for the LCSS page for the compound
    lcss_url = f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}#datasheet=LCSS"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Set up WebDriver using ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Load the LCSS page
        driver.get(lcss_url)

        # Wait extra time to ensure the entire page has loaded
        time.sleep(5)

        # Get page source after content has loaded
        page_source = driver.page_source

    except Exception as e:
        print(f"Error fetching LCSS data for CID {cid}: {e}")
        page_source = None

    finally:
        # Close the driver
        driver.quit()

    return page_source

def parse_lcss_data(cid, html_content):
    # Parse the LCSS page content to extract safety-related information
    soup = BeautifulSoup(html_content, 'html.parser')
    safety_info = []

    # Extract GHS hazard icons (with alt attributes containing labels like "Irritant", "Flammable", etc.)
    hazard_icons = soup.find_all('img', alt=True)
    for icon in hazard_icons:
        alt_text = icon.get('alt')
        if alt_text and any(keyword in alt_text.lower() for keyword in ['irritant', 'corrosive', 'flammable', 'hazard', 'toxic', 'danger']):
            safety_info.append(alt_text)

    print(f"\nChecking safety data for CID: {cid}")
    if not safety_info:
        print("No specific safety information found for this compound.")
    else:
        print("Safety Information:")
        for info in safety_info:
            print(f"- {info}")

# List of CIDs to test
cid_list = [2244, 1983, 1234]  # Replace with the CIDs you want to test

# Iterate over each CID and fetch & parse the LCSS data
for cid in cid_list:
    html_content = fetch_lcss_data(cid)
    if html_content:
        parse_lcss_data(cid, html_content)
