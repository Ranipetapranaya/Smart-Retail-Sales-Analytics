import pandas as pd

# Read the original dataset
data = pd.read_excel("retail_original_dataset.xlsx")

print("Original dataset:", data.shape)

# Remove duplicate rows
data = data.drop_duplicates()

# Remove rows with missing values
data = data.dropna()

# Remove unwanted columns if they exist
data = data.drop(
    columns=["Daily Percentage Change", "Year"],
    errors="ignore"
)

# Create Month from Date
data["Date"] = pd.to_datetime(data["Date"], dayfirst=True)
data["Month"] = data["Date"].dt.strftime("%b")

# Create Age Group
def get_age_group(age):
    if age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    elif age <= 55:
        return "46-55"
    else:
        return "56-64"

data["Age Group"] = data["Age"].apply(get_age_group)

# Keep the exact required column order
columns = [
    "Transaction ID",
    "Date",
    "Customer ID",
    "Gender",
    "Age",
    "Product Category",
    "Quantity",
    "Price per Unit",
    "Total Amount",
    "Month",
    "Age Group"
]

data = data[columns]

# Save the cleaned dataset
data.to_csv("cleaned_retail_sales.csv", index=False)

print("Cleaned dataset:", data.shape)
print("\nFinal columns:")
print(data.columns.tolist())
print("\nCleaned dataset saved successfully!")
