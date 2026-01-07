import streamlit as st
import numpy as np
import joblib

st.title("Student Pass/Fail Prediction System")

st.write("Enter student academic scores to predict outcome.")

math = st.slider("Math Score", 0, 100, 75)
reading = st.slider("Reading Score", 0, 100, 75)
writing = st.slider("Writing Score", 0, 100, 75)

if st.button("Predict"):
    avg_score = np.mean([math, reading, writing])
    
    if avg_score >= 90:
        st.success("Prediction: PASS")
    else:
