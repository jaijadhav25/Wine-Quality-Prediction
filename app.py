import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("wine_quality_model.pkl")

st.title("🍷 Wine Quality Prediction App")

st.write("Enter wine chemical properties:")

# User Inputs
fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0, 7.5)
volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.5)
citric_acid = st.number_input("Citric Acid", 0.0, 1.0, 0.36)
residual_sugar = st.number_input("Residual Sugar", 0.0, 20.0, 6.1)
chlorides = st.number_input("Chlorides", 0.0, 1.0, 0.071)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", 0.0, 100.0, 17.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", 0.0, 300.0, 102.0)
density = st.number_input("Density", 0.9900, 1.0100, 0.9978)
pH = st.number_input("pH", 2.0, 4.5, 3.35)
sulphates = st.number_input("Sulphates", 0.0, 2.0, 0.8)
alcohol = st.number_input("Alcohol", 5.0, 20.0, 10.5)

# Predict Button
if st.button("Predict Quality"):

    input_data = (
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
    )

    input_array = np.asarray(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.success("🍷 Good Quality Wine")
    else:
        st.error("⚠️ Bad Quality Wine")