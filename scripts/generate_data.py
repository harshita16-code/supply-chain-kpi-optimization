import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# ----------------------------
# Configurations
# ----------------------------
NUM_ORDERS = 500  # Number of fake orders
RAW_DATA_PATH = "../data/raw/orders.csv"

# Ensure directory exists
os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)

# ----------------------------
# Fake Data Generators
# ----------------------------
vendors = ["Tata Steel", "Flipkart Logistics", "Amazon Supply", "BizAd Ltd.", "Global Traders"]
products = ["Laptops", "Mobiles", "Steel Rods", "Shoes", "FMCG", "Furniture", "Electronics"]

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date(start, end):
    """Generate random datetime between two datetime objects."""
    return start + timedelta(days=random.randint(0, (end - start).days))

# ----------------------------
# Generate Orders
# ----------------------------
orders = []
for i in range(1, NUM_ORDERS+1):
    order_date = random_date(start_date, end_date)
    promised_date = order_date + timedelta(days=random.randint(3, 15))
    actual_date = promised_date + timedelta(days=random.choice([-2, -1, 0, 1, 2, 3, 5]))

    orders.append({
        "OrderID": f"ORD{i:04d}",
        "Vendor": random.choice(vendors),
        "Product": random.choice(products),
        "Quantity": random.randint(1, 500),
        "OrderDate": order_date.strftime("%Y-%m-%d"),
        "PromisedDate": promised_date.strftime("%Y-%m-%d"),
        "ActualDeliveryDate": actual_date.strftime("%Y-%m-%d"),
        "Status": "Delivered" if actual_date <= datetime.now() else "Pending"
    })

# ----------------------------
# Save to CSV
# ----------------------------
df = pd.DataFrame(orders)
df.to_csv(RAW_DATA_PATH, index=False)

print(f"✅ Fake supply chain dataset generated: {RAW_DATA_PATH}")
