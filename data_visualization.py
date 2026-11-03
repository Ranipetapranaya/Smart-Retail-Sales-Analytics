import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
data = pd.read_csv("cleaned_retail_sales.csv")

# 1. Sales by Product Category
category_sales = data.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(8, 5))
bars = plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Amount")
plt.bar_label(bars, fmt="%.0f")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 2. Monthly Sales Trend
month_order = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

monthly_sales = data.groupby("Month")["Total Amount"].sum()
monthly_sales = monthly_sales.reindex(month_order).dropna()

plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 3. Sales by Age Group
age_order = ["18-25", "26-35", "36-45", "46-55", "56-64"]

age_sales = data.groupby("Age Group")["Total Amount"].sum()
age_sales = age_sales.reindex(age_order).dropna()

plt.figure(figsize=(8, 5))
bars = plt.bar(age_sales.index, age_sales.values)
plt.title("Sales by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Amount")
plt.bar_label(bars, fmt="%.0f")
plt.tight_layout()
plt.savefig("age_group_sales.png")
plt.show()

# 4. Sales by Gender
gender_sales = data.groupby("Gender")["Total Amount"].sum()

plt.figure(figsize=(8, 5))
bars = plt.barh(gender_sales.index, gender_sales.values)
plt.title("Sales by Gender")
plt.xlabel("Total Amount")
plt.ylabel("Gender")
plt.bar_label(bars, fmt="%.0f")
plt.tight_layout()
plt.savefig("gender_sales.png")
plt.show()

print("All four dashboard visualizations created successfully!")