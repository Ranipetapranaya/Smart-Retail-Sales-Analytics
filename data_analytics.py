import pandas as pd

# Load the cleaned dataset
data = pd.read_csv("cleaned_retail_sales.csv")

print("SMART RETAIL SALES ANALYTICS")
print("-" * 35)

# Calculate total sales
print("\nTotal Sales:")
print(data["Total Amount"].sum())

# Sales by product category
print("\nSales by Product Category:")
print(data.groupby("Product Category")["Total Amount"].sum())

# Sales by gender
print("\nSales by Gender:")
print(data.groupby("Gender")["Total Amount"].sum())

# Sales by month in calendar order
month_order = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

monthly_sales = data.groupby("Month")["Total Amount"].sum()
monthly_sales = monthly_sales.reindex(month_order).dropna()

print("\nMonthly Sales:")
print(monthly_sales)

# Sales by age group
print("\nSales by Age Group:")
print(data.groupby("Age Group")["Total Amount"].sum())

print("\nAnalytics completed successfully!")
