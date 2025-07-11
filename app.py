# app.py

import streamlit as st
import joblib

# Load trained model
model = joblib.load("liquidity_model.pkl")

# Title
st.title("Cryptocurrency Liquidity Predictor")
st.markdown("Predict real-time **market liquidity** using historical trading indicators.")

# Input fields
volume = st.number_input("24h Volume", min_value=0.0, format="%.6f")
ma_7 = st.number_input("7-Day Moving Average", min_value=0.0, format="%.6f")
volatility = st.number_input("Price Volatility", min_value=0.0, format="%.6f")
liq_ratio = st.number_input("Liquidity Ratio (Volume / Volatility)", min_value=0.0, format="%.6f")

# Prediction button
if st.button("Predict Liquidity"):
    input_data = [[volume, ma_7, volatility, liq_ratio]]
    prediction = model.predict(input_data)[0]
    st.success(f" Predicted Liquidity: `{prediction:.6f}`")
