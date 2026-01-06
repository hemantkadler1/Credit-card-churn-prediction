import streamlit as st
import pandas as pd
import requests

st.title("Credit Card Customer Churn Prediction")

df = pd.read_csv("Dataset(BankChurners)_CampusHiring_Dec2025(dataset).csv")

st.subheader("Dataset Information")
st.write("Shape of dataset:", df.shape)
st.write("Columns:", list(df.columns))

st.subheader("Enter Customer Details")

credit_limit = st.number_input("Credit Limit", min_value=0.0)
total_trans_amt = st.number_input("Total Transaction Amount", min_value=0.0)
total_trans_ct = st.number_input("Total Transaction Count", min_value=0)
months_inactive = st.number_input("Months Inactive (Last 12 Months)", min_value=0)
avg_utilization = st.number_input("Average Utilization Ratio", min_value=0.0, max_value=1.0)

if st.button("Predict Churn"):
    payload = {
        "Credit_Limit": credit_limit,
        "Total_Trans_Amt": total_trans_amt,
        "Total_Trans_Ct": total_trans_ct,
        "Months_Inactive_12_mon": months_inactive,
        "Avg_Utilization_Ratio": avg_utilization
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['message']}")
    else:
        st.error("Error calling prediction API")
