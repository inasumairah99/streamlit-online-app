import streamlit as st
import numpy as np

# Blue colored title
st.markdown("<h1 style='color:blue;'>Student Pass/Fail Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter student academic scores to predict outcome:")

# -------------------------
# Number input boxes for each subject
math = st.number_input("Math Score", min_value=0, max_value=100, value=75)
reading = st.number_input("Reading Score", min_value=0, max_value=100, value=75)
writing = st.number_input("Writing Score", min_value=0, max_value=100, value=75)

# -------------------------
if st.button("Predict"):
    avg_score = np.mean([math, reading, writing])
    
    if avg_score >= 90:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")

