# bmi_calculator.py

import streamlit as st

# Title of the app
st.title("BMI Calculator")

# User input for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=1.0, max_value=200.0, value=70.0)
height = st.number_input("Enter your height (in meters):", min_value=0.5, max_value=2.5, value=1.75)

# Calculate BMI
if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Display BMI category
    if bmi < 18.5:
        st.write("Category: Underweight")

    elif 18.5 <= bmi < 24.9:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obese")
else:
    st.write("Height must be greater than zero to calculate BMI.")
