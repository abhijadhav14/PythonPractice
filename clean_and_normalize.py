import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json

# Read the CSV file
df = pd.read_csv('file.csv')

# Handle missing values (fill with 0 for example)
df.fillna(0, inplace=True)

# Normalize a specific numerical column (e.g., 'numerical_column')
scaler = MinMaxScaler()
column_to_normalize = 'numerical_column'
df[[column_to_normalize]] = scaler.fit_transform(df[[column_to_normalize]])

# Convert the DataFrame to a dictionary
data_dict = df.to_dict(orient='records')

# Write the dictionary to a JSON file
with open('cleaned_normalized_data.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

# Print the first few rows to check the result
print(df.head())

