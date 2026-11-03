import pandas as pd

# Data Collection: Read the original retail dataset
file_name = "retail_original_dataset.xlsx"

# Load the dataset
data = pd.read_excel(file_name)

# Display dataset details
print("SMART RETAIL SALES ANALYTICS")
print("----------------------------")

print("\nDataset Source: Kaggle")
print("Dataset Name:", file_name)

# Display number of rows and columns
print("\nNumber of Rows:", data.shape[0])
print("Number of Columns:", data.shape[1])

# Display column names
print("\nColumn Names:")
print(data.columns.tolist())

# Display first five records
print("\nFirst Five Records:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
data.info()

# Display missing values
print("\nMissing Values:")
print(data.isnull().sum())

print("\nData Collection Completed Successfully!")
