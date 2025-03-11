import sqlite3
import pandas as pd

# Load Data
suppliers = pd.read_csv("data/supplier_data.csv")
reviews = pd.read_csv("data/customer_reviews_with_sentiment.csv")
country_risk = pd.read_csv("data/country_risk.csv")

# Compute average sentiment per part
avg_sentiment = reviews.groupby("part_number")["sentiment_score"].mean().reset_index()

# Merge sentiment into supplier data
suppliers["average_quality"] = suppliers["part_numbers"].apply(
    lambda x: avg_sentiment[avg_sentiment["part_number"].isin(x.split(","))]["sentiment_score"].mean() if x else 0.5
)

# Merge country risk data
suppliers = suppliers.merge(country_risk, on="country", how="left")

# Save as SQLite DB
conn = sqlite3.connect("data/supplier_risk.db")
suppliers.to_sql("supplier_risk_assessment", conn, if_exists="replace", index=False)
reviews.to_sql("customer_reviews", conn, if_exists="replace", index=False)
country_risk.to_sql("country_risk", conn, if_exists="replace", index=False)
conn.close()

print("✅ Database schema created successfully.")
