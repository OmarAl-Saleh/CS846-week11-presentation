# Optimized Sales Revenue Aggregator
#
# This function processes sales records and returns total revenue per category.
# Optimized for better performance on large datasets.

import random
import time
from collections import defaultdict
from datetime import datetime
import math


def generate_records(n=500_000):
    random.seed(42)
    categories = ["Electronics", "Clothing", "Food", "Books", "Sports",
                  "Home", "Beauty", "Toys", "Garden", "Auto"]
    regions = ["North", "South", "East", "West", "Central"]
    methods = ["credit", "debit", "cash", "paypal"]

    records = []
    for i in range(n):
        records.append({
            "transaction_id": f"TXN-{i:07d}",
            "date": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "category": random.choice(categories),
            "unit_price": round(random.uniform(1, 500), 2),
            "quantity": random.randint(1, 20),
            "customer_id": f"CUST-{random.randint(1, 10000):05d}",
            "region": random.choice(regions),
            "payment_method": random.choice(methods),
        })
    return records


def get_revenue_by_category(records):
    """Process sales records and return total revenue per category."""

    # Step 1: Validate records using a generator
    required_keys = {"transaction_id", "date", "category", "unit_price",
                     "quantity", "customer_id", "region", "payment_method"}
    valid_records = (
        record for record in records
        if required_keys.issubset(record)
        and record["unit_price"] is not None
        and record["quantity"] is not None
    )

    # Step 2: Group by category and compute stats
    category_data = defaultdict(lambda: {
        "total_revenue": 0,
        "total_price": 0,
        "total_quantity": 0,
        "revenue_squared": 0,
        "revenues": [],
        "unique_customers": set(),
        "regions": set(),
    })

    for record in valid_records:
        cat = record["category"]
        revenue = record["unit_price"] * record["quantity"]

        data = category_data[cat]
        data["total_revenue"] += revenue
        data["total_price"] += record["unit_price"]
        data["total_quantity"] += record["quantity"]
        data["revenue_squared"] += revenue ** 2
        data["revenues"].append(revenue)
        data["unique_customers"].add(record["customer_id"])
        data["regions"].add(record["region"])

    # Step 3: Compute detailed statistics per category
    result = {}
    for cat, data in category_data.items():
        n = len(data["revenues"])
        avg_price = data["total_price"] / n
        avg_quantity = data["total_quantity"] / n
        std_rev = math.sqrt((data["revenue_squared"] / n) - (data["total_revenue"] / n) ** 2)
        median_rev = sorted(data["revenues"])[n // 2] if n % 2 == 1 else (
            sorted(data["revenues"])[n // 2 - 1] + sorted(data["revenues"])[n // 2]) / 2

        result[cat] = {
            "total_revenue": round(data["total_revenue"], 2),
            "average_price": round(avg_price, 2),
            "average_quantity": round(avg_quantity, 2),
            "std_dev_revenue": round(std_rev, 2),
            "median_revenue": round(median_rev, 2),
            "unique_customers": len(data["unique_customers"]),
            "region_count": len(data["regions"]),
        }

    return result


records = generate_records()

start = time.perf_counter()
result = get_revenue_by_category(records)
elapsed = time.perf_counter() - start

for cat, data in sorted(result.items()):
    print(f"{cat}: ${data['total_revenue']:,.2f}")

print(f"\nTime: {elapsed:.3f}s")
