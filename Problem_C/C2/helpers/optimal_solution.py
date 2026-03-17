import random
import time

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
    result = {}
    for record in records:
        cat = record["category"]
        revenue = record["unit_price"] * record["quantity"]
        if cat not in result:
            result[cat] = {"total_revenue": 0}
        result[cat]["total_revenue"] += revenue

    for cat in result:
        result[cat]["total_revenue"] = round(result[cat]["total_revenue"], 2)

    return result

records = generate_records()

start = time.perf_counter()
result = get_revenue_by_category(records)
elapsed = time.perf_counter() - start

for cat, data in sorted(result.items()):
    print(f"{cat}: ${data['total_revenue']:,.2f}")

print(f"\nTime: {elapsed:.3f}s")
