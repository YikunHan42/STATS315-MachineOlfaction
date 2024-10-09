import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace this with the actual file path)
file_path = './Kit.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Split the odor descriptors into sets for easier comparison
data['Odor (Michelle)'] = data['Odor (from Michelle, intersect with 138 labels)'].str.split(', ').apply(set)
data['Odor (Prediction)'] = data['Odor (from prediction)'].str.split(', ').apply(set)

# Create a set of all unique odor descriptors in both Michelle's and Prediction columns
all_odors = sorted(set(odor for odors in data['Odor (Michelle)'] for odor in odors).union(
    odor for odors in data['Odor (Prediction)'] for odor in odors))

# Initialize the heatmap matrix
heatmap_data = np.zeros((len(data), len(all_odors)))

# Populate the matrix: 1 if odor is present in 'Michelle', 2 if in 'Prediction', 3 if in both
for i, row in data.iterrows():
    for j, odor in enumerate(all_odors):
        if odor in row['Odor (Michelle)'] and odor in row['Odor (Prediction)']:
            heatmap_data[i, j] = 3  # Present in both
        elif odor in row['Odor (Michelle)']:
            heatmap_data[i, j] = 1  # Present in Michelle's labels
        elif odor in row['Odor (Prediction)']:
            heatmap_data[i, j] = 2  # Present in Predictions

# Creating the heatmap
plt.figure(figsize=(12, 8))
ax = sns.heatmap(heatmap_data, cmap='coolwarm', cbar_kws={'ticks': [0, 1, 2, 3], 'label': 'Presence'},
                 xticklabels=all_odors, yticklabels=data['Compound'], linewidths=.5, linecolor='gray')

ax.set_xlabel('Odor Descriptor')
ax.set_ylabel('Compound')
ax.set_title('Heatmap of Odor Descriptor Agreement between Expert and Prediction')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the heatmap
plt.show()
