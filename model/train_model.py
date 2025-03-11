import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ✅ Load Supplier Data
df = pd.read_csv("data/supplier_data.csv")

# ✅ Load Country Risk Data and Merge with Supplier Data
country_risk = pd.read_csv("data/country_risk.csv")
df = df.merge(country_risk, on="country", how="left")  # Ensure risk_rank is added

# ✅ Verify Columns
print("Columns in Data:", df.columns)

# ✅ Define Risk Label (Binary Classification)
df["risk_label"] = ((df["faults_last_18m"] * 0.4) + ((10 - df["financial_score"]) * 0.3) + ((5 - df["risk_rank"]) * 0.3)) > 7
df["risk_label"] = df["risk_label"].astype(int)  # Convert to binary (0 = Safe, 1 = Risky)

# ✅ Select Features & Target
features = ["faults_last_18m", "financial_score", "quality_rating", "backup_suppliers", "risk_rank"]
X = df[features]
y = df["risk_label"]

# ✅ Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Initialize and Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save Model
with open("model/risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as `risk_model.pkl`")
