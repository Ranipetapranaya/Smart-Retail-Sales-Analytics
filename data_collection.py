import pandas as pd

# Data Collection: Read the original retail dataset
file_name = "retail_original_dataset.xlsx"

data = pd.read_excel(file_name)

# Display dataset information
print("SMART RETAIL SALES ANALYTICS")
print("----------------------------")

print("\nDataset collected successfully!")

print("\nDataset Name:", file_name)

print("\nNumber of Rows:", data.shape[0])

print("Number of Columns:", data.shape[1])

print("\nColumn Names:")
print(data.columns.tolist())

print("\nFirst Five Records:")
print(data.head())

print("\nDataset Information:")
data.info()

print("\nMissing Values:")
print(data.isnull().sum())

print("\nData Collection Completed Successfully!")