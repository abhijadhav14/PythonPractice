import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the Iris dataset
iris = pd.read_csv('../data/iris.csv')  # Adjusting the path to iris.csv

# Create the eda_results directory if it doesn't exist
os.makedirs('eda_results', exist_ok=True)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(iris.head())

# Summary statistics of numerical columns
summary_stats = iris.describe()
print("\nSummary statistics of numerical columns:")
print(summary_stats)

# Save summary statistics to a text file
summary_stats.to_csv('eda_results/iris_summary_statistics.txt', sep='\t')

# Information about the dataset
info = str(iris.info())
print("\nInformation about the dataset:")
print(info)
with open('eda_results/iris_info.txt', 'w') as info_file:
    info_file.write(info)

# Encode the 'variety' column to numerical values using LabelEncoder
label_encoder = LabelEncoder()
iris['variety_encoded'] = label_encoder.fit_transform(iris['variety'])

# Histograms for each feature
plt.figure(figsize=(10, 6))
for i, col in enumerate(iris.columns[:-2]):
    plt.subplot(2, 2, i+1)
    sns.histplot(iris[col], kde=True)
    plt.title(f'Histogram of {col}')
plt.tight_layout()
plt.savefig('eda_results/histograms.png')
plt.close()

# Pairplot for all features colored by variety (species)
pairplot = sns.pairplot(iris, hue='variety', height=2.5)
pairplot.savefig('eda_results/pairplot.png')
plt.close()

# Correlation heatmap
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
heatmap.set_title("Correlation Heatmap of Iris Dataset")
plt.savefig('eda_results/correlation_heatmap.png')
plt.close()
