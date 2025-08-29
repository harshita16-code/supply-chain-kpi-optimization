# scripts/kpi_calculator.py

import pandas as pd
import os

# Paths
RAW_DATA_PATH = os.path.join("data", "raw", "orders.csv")
PROCESSED_PATH = os.path.join("data", "processed")
OUTPUT_FILE = os.path.join(PROCESSED_PATH, "kpis.csv")

# Make sure processed folder exists
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load raw data
orders = pd.read_csv(RAW_DATA_PATH)

# --- KPI Calculations ---
# 1. Total Revenue
total_revenue = orders["TotalAmount"].sum()

# 2. Average Order Value
avg_order_value = orders["TotalAmount"].mean()

# 3. Orders per Customer
orders_per_customer = orders.groupby("CustomerID")["OrderID"].count().mean()

# 4. On-Time Delivery %
on_time_pct = (orders["DeliveryStatus"] == "On Time").mean() * 100

# 5. Top 5 Products by Revenue
top_products = (
    orders.groupby("ProductID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# --- Save KPI Results ---
kpi_results = pd.DataFrame({
    "Metric": ["Total Revenue", "Average Order Value", "Orders per Customer", "On-Time Delivery %"],
    "Value": [total_revenue, avg_order_value, orders_per_customer, on_time_pct]
})

kpi_results.to_csv(OUTPUT_FILE, index=False)

# Save Top Products separately
top_products.to_csv(os.path.join(PROCESSED_PATH, "top_products.csv"))

print("✅ KPI results saved in:", OUTPUT_FILE)
print("✅ Top products saved in: data/processed/top_products.csv")
