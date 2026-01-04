import streamlit as st
import numpy as np

# Blue colored title
st.markdown("<h1 style='color:blue;'>Student Pass/Fail Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter student academic scores to predict outcome. You can use the slider or enter the marks in the box.")

# -------------------------
# Function to get input from slider or text box
def get_score(subject, default=75):
    col1, col2 = st.columns([3,1])  # slider wider, box smaller
    with col1:
        score_slider = st.slider(f"{subject} Score (Slider)", 0, 100, default, key=f"{subject}_slider")
    with col2:
        score_input = st.number_input(f"{subject} Score (Box)", min_value=0, max_value=100, value=default, key=f"{subject}_input")
    
    # If user enters in box, use that; otherwise use slider
    # Prioritize text input if it is different from default
    if score_input != default:
        return score_input
    else:
        return score_slider

# Get scores
math = get_score("Math")
reading = get_score("Reading")
writing = get_score("Writing")

# -------------------------
if st.button("Predict"):
    avg_score = np.mean([math, reading, writing])
    
    if avg_score >= 90:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")

