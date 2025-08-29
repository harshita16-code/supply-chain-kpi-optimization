import pandas as pd
import numpy as np
import os

# Save path (adjust if needed)
RAW_DATA_PATH = "../data/raw/orders.csv"

# Ensure folder exists
os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)

# Generate sample order data
np.random.seed(42)  # reproducible
num_records = 200

df = pd.DataFrame({
    "OrderID": range(1, num_records + 1),
    "Product": np.random.choice(
        ["Laptop", "Phone", "Headphones", "Tablet", "Monitor", "Keyboard"], 
        num_records
    ),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], 
        num_records
    ),
    "OrderQuantity": np.random.randint(1, 10, num_records),
    "UnitPrice": np.random.randint(200, 2000, num_records),
    "OrderDate": pd.date_range(start="2023-01-01", periods=num_records, freq="D")
})

# Calculate revenue
df["Revenue"] = df["OrderQuantity"] * df["UnitPrice"]

# Save to CSV
df.to_csv(RAW_DATA_PATH, index=False)

print(f"✅ orders.csv created at {RAW_DATA_PATH} with {len(df)} rows")
