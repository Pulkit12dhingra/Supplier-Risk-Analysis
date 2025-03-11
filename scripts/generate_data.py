import pandas as pd
import numpy as np
import random

# Define random seed for reproducibility
np.random.seed(42)

# Generate Supplier Data
num_suppliers = 50
suppliers = pd.DataFrame({
    "supplier_id": range(1, num_suppliers + 1),
    "part_numbers": [",".join([f"P{random.randint(100, 999)}" for _ in range(random.randint(1, 5))]) for _ in range(num_suppliers)],
    "business_level": np.random.randint(1, 5, num_suppliers),
    "backup_suppliers": np.random.randint(0, 6, num_suppliers),
    "country": np.random.choice(["USA", "China", "Germany", "India", "Mexico"], num_suppliers),
    "faults_last_18m": np.random.randint(0, 21, num_suppliers),
    "shipping_plants": [",".join([f"Plant {random.randint(1, 5)}" for _ in range(random.randint(1, 3))]) for _ in range(num_suppliers)],
    "inventory_capacity": np.random.randint(100, 10000, num_suppliers),
    "quality_rating": np.random.uniform(0, 1, num_suppliers).round(2),
    "financial_score": np.random.uniform(0, 10, num_suppliers).round(2),
})

# Generate Customer Reviews Data
num_reviews = 200
reviews = pd.DataFrame({
    "review_id": range(1, num_reviews + 1),
    "part_number": [f"P{random.randint(100, 999)}" for _ in range(num_reviews)],
    "review_text": np.random.choice([
        "Excellent quality, very satisfied!", "Terrible experience, defective parts!",
        "Shipping took too long, but good quality.", "Perfect! Will buy again.",
        "Mediocre at best.", "Supplier is unreliable.", "Great service and prompt delivery."
    ], num_reviews)
})

# Generate Country Risk Data
country_risk = pd.DataFrame({
    "country": ["USA", "China", "Germany", "India", "Mexico"],
    "risk_rank": [3, 1, 4, 2, 2]  # Lower rank = higher risk
})

# Save as CSV
suppliers.to_csv("data/supplier_data.csv", index=False)
reviews.to_csv("data/customer_reviews.csv", index=False)
country_risk.to_csv("data/country_risk.csv", index=False)

print("✅ Synthetic data generated and saved.")
