"""
Sales Data Analysis - beginner project
Run: python sales_analysis.py
Dataset: sales_data.csv (small sample dataset created for learning)
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("sales_data.csv")
OUTPUT_DIR = Path(__file__).with_name("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load the data
df = pd.read_csv(DATA_FILE, parse_dates=["Date"])

# 2. Inspect and clean the data
print("First five rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isna().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["Date", "Product", "Quantity", "UnitPrice"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# 3. Summarize the data
total_revenue = df["Revenue"].sum()
total_units = df["Quantity"].sum()
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
monthly_revenue = (
    df.set_index("Date")
      .resample("MS")["Revenue"]
      .sum()
)

print(f"\nTotal revenue in sample data: ₹{total_revenue:,.2f}")
print(f"Total units sold in sample data: {total_units}")
print("\nRevenue by product:")
print(top_products)
print("\nMonthly revenue:")
print(monthly_revenue)

# 4. Save summary tables
top_products.rename("Revenue").to_csv(OUTPUT_DIR / "revenue_by_product.csv")
monthly_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "monthly_revenue.csv")

# 5. Create charts
top_products.sort_values().plot(kind="barh", title="Revenue by Product")
plt.xlabel("Revenue (₹)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_by_product.png", dpi=150)
plt.close()

monthly_revenue.plot(kind="line", marker="o", title="Monthly Revenue")
plt.ylabel("Revenue (₹)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

print(f"\nAnalysis complete. Check the '{OUTPUT_DIR.name}' folder for output files.")
