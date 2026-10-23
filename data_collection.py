import pandas as pd

# Load the retail sales dataset
file_name = "retail sales dataset.xlsx"

data = pd.read_excel(file_name)

# Display the collected data
print("DATA COLLECTION")
print("Dataset loaded successfully!")

print("\nFirst 5 rows:")
print(data.head())

print("\nNumber of rows and columns:")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())
