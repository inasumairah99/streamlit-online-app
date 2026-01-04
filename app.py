import streamlit as st
import numpy as np

st.markdown("<h1 style='color:blue;'>Student Pass/Fail Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter student academic scores to predict outcome.")

math = st.slider("Math Score", 0, 100, 75)
reading = st.slider("Reading Score", 0, 100, 75)
writing = st.slider("Writing Score", 0, 100, 75)

if st.button("Predict"):
    avg_score = np.mean([math, reading, writing])
    
    if avg_score >= 90:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")
