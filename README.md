# 📊 Supplier Risk Analysis

🚀 A **Supplier Risk Analysis** system that helps assess supplier risks based on **financial, operational, and compliance factors**. It features a **machine learning model for risk prediction** and an **interactive Streamlit dashboard**.

---

## 📌 Project Overview
This project evaluates **supplier risks** using:
✅ **Supplier Data** (e.g., financial score, fault history)  
✅ **Customer Sentiment Analysis** (NLP on reviews)  
✅ **Country Risk Ranking** (External data)  
✅ **Machine Learning** (Predicts risky suppliers)  
✅ **Interactive Dashboard** (Streamlit-powered visualization)  

---

## 📁 File Structure
📁 SupplierRiskAnalysis/ │── 📁 data/ # Stores raw & processed data │ ├── supplier_data.csv │ ├── customer_reviews.csv │ ├── country_risk.csv │── 📁 scripts/ # Data processing scripts │ ├── generate_data.py # Generates synthetic data │ ├── generate_sentiment.py # Runs sentiment analysis on reviews │ ├── get_schema.py # Builds star schema │── 📁 models/ # Machine learning model │ ├── train_model.py # Trains risk prediction model │ ├── risk_model.pkl # Saved trained model ├── app.py # Main Streamlit dashboard │── requirements.txt # Project dependencies │── README.md # Documentation │── .gitignore # Ignore unnecessary files

yaml
Copy
Edit

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/supplier-risk-analysis.git
cd supplier-risk-analysis
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Generate Data
bash
Copy
Edit
python scripts/generate_data.py
python scripts/generate_sentiment.py
python scripts/get_schema.py
4️⃣ Train the Machine Learning Model
bash
Copy
Edit
python models/train_model.py
5️⃣ Run the Streamlit Dashboard
bash
Copy
Edit
streamlit run app/dashboard.py
📊 Features
🔹 Data Processing
✅ Supplier Data Generation (synthetic dataset)
✅ Sentiment Analysis on Reviews (VADER NLP model)
✅ Country Risk Ranking (geopolitical risk factor)
🔹 Machine Learning
✅ RandomForestClassifier Model (predicts high-risk suppliers)
✅ Risk Scoring Formula (weighted metrics)
✅ Feature Engineering (faults, financials, inventory)
🔹 Interactive Dashboard
✅ KPIs: Total suppliers, Risky suppliers, Country count
✅ Filters: By KPI and Country
✅ Bar Chart: Risky suppliers per country
✅ Table View: High-risk suppliers