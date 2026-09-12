import streamlit as st
import pandas as pd
import joblib

# Load trained Random Forest model
model = joblib.load("random_forest_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Grocery Sales Prediction",
    page_icon="🛒",
    layout="centered"
)

# Title
st.title("🛒 Grocery Store Sales Prediction")

st.write(
    "Daily sales prediction for Store 44 - GROCERY I "
    "using Random Forest Regression."
)

st.divider()

# Input section
st.header("Enter Prediction Details")

onpromotion = st.number_input(
    "Number of Products on Promotion",
    min_value=0,
    value=20,
    step=1
)

year = st.number_input(
    "Year",
    min_value=2013,
    max_value=2030,
    value=2017,
    step=1
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=8,
    step=1
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=16,
    step=1
)

day_of_week = st.selectbox(
    "Day of Week",
    options=[0, 1, 2, 3, 4, 5, 6],
    format_func=lambda x: [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ][x]
)

st.divider()

# Prediction button
if st.button("🔮 Predict Sales"):

    input_data = pd.DataFrame({
        "onpromotion": [onpromotion],
        "year": [year],
        "month": [month],
        "day": [day],
        "day_of_week": [day_of_week]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"📊 Predicted Grocery Sales: {prediction:,.2f}"
    )

    st.info(
        "This prediction is generated using the trained "
        "Random Forest Regression model."
    )