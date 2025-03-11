import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ✅ Fix: Set page config as the first Streamlit command
st.set_page_config(layout="wide", page_title="Supplier Risk Dashboard")

# Connect to database
conn = sqlite3.connect("data/supplier_risk.db")
df = pd.read_sql("SELECT * FROM supplier_risk_assessment", conn)
conn.close()
print("database Connected")

# Risk Score Calculation
df["risk_score"] = (df["faults_last_18m"] * 0.4) + ((10 - df["financial_score"]) * 0.3) + ((5 - df["risk_rank"]) * 0.3)

# Define Risk Threshold
risky_threshold = 7

# **Sidebar Filters**
st.sidebar.header("🔹 Filters")

# KPI Selection
selected_kpi = st.sidebar.radio(
    "Choose KPI to Filter Data:",
    ["Total Suppliers", "Risky Suppliers"]
)

# Country Selection
country_options = ["All"] + sorted(df["country"].unique().tolist())
selected_country = st.sidebar.selectbox("Filter by Country:", country_options)

# **Filter Data Based on Selections**
if selected_kpi == "Total Suppliers":
    filtered_df = df
    title_suffix = "All Suppliers"
else:
    filtered_df = df[df["risk_score"] > risky_threshold]
    title_suffix = "Risky Suppliers Only"

# Apply Country Filter
if selected_country != "All":
    filtered_df = filtered_df[filtered_df["country"] == selected_country]

# **Recalculate KPI Metrics**
total_suppliers = df.shape[0]
num_risky_suppliers = df[df["risk_score"] > risky_threshold].shape[0]
num_countries = df["country"].nunique()

# **KPI Metrics**
st.title("📊 Supplier Risk Dashboard")

st.markdown("### Key Metrics (Click to Filter)")
col1, col2 = st.columns([1, 1])

if col1.button(f"Total Suppliers ({total_suppliers})"):
    selected_kpi = "Total Suppliers"

if col2.button(f"Risky Suppliers ({num_risky_suppliers})"):
    selected_kpi = "Risky Suppliers"

st.markdown(f"### Viewing Data: {title_suffix} - {selected_country if selected_country != 'All' else 'All Countries'}")
st.markdown("---")

# **Bar Chart: Suppliers by Country (Filtered)**
risky_by_country = filtered_df["country"].value_counts().reset_index()
risky_by_country.columns = ["country", "supplier_count"]
fig_bar = px.bar(
    risky_by_country, x="country", y="supplier_count",
    title=f"Number of {title_suffix} per Country",
    color="supplier_count", color_continuous_scale="reds"
)

st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# **Table View: Filtered Suppliers**
st.markdown(f"### {title_suffix} - {selected_country if selected_country != 'All' else 'All Countries'} (Top 10)")
st.dataframe(filtered_df.sort_values(by="risk_score", ascending=False).head(10))

st.success("✅ Dashboard Loaded Successfully!")
