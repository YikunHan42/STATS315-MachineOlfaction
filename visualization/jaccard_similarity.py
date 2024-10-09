import pandas as pd
import matplotlib.pyplot as plt

# Define the Jaccard similarity function
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Load the dataset (replace this with the actual file path)
file_path = './Kit.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Split the odor descriptors into sets for easier comparison
data['Odor (Michelle)'] = data['Odor (from Michelle, intersect with 138 labels)'].str.split(', ').apply(set)
data['Odor (Prediction)'] = data['Odor (from prediction)'].str.split(', ').apply(set)

# Apply the Jaccard similarity calculation to each row
data['Jaccard Similarity'] = data.apply(lambda row: jaccard_similarity(row['Odor (Michelle)'], row['Odor (Prediction)']), axis=1)

# Creating a bar plot for Jaccard Similarity Scores
plt.figure(figsize=(10, 6))
plt.bar(data['Compound'], data['Jaccard Similarity'], color='skyblue')
plt.xlabel('Compound')
plt.ylabel('Jaccard Similarity Score')
plt.title('Jaccard Similarity Between Expert and Prediction Odors')
plt.xticks(rotation=90)
plt.ylim(0, 1)
plt.tight_layout()

# Display the plot
plt.show()
