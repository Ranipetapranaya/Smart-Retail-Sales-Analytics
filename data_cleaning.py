import pandas as pd

data = pd.read_excel("retail_original_dataset.xlsx")

print("Before cleaning:", data.shape)

data = data.drop_duplicates()
data = data.dropna()

data.to_csv("cleaned_retail_sales.csv", index=False)

print("After cleaning:", data.shape)
print("Cleaned data saved successfully!")
