import streamlit as st
import numpy as np

# Blue colored title
st.markdown("<h1 style='color:blue;'>Student Pass/Fail Prediction System</h1>", unsafe_allow_html=True)

st.write("Enter student academic scores to predict outcome. You can use the slider or type the marks in the box.")

# -------------------------
# Function to get synced slider + number input (no label on input box)
def get_synced_score(subject, default=75):
    # Initialize session state
    if f"{subject}_score" not in st.session_state:
        st.session_state[f"{subject}_score"] = default

    col1, col2 = st.columns([3,1])

    # Slider with label
    with col1:
        slider_val = st.slider(f"{subject} Score", 0, 100, value=st.session_state[f"{subject}_score"], key=f"{subject}_slider")
    # Number input WITHOUT label
    with col2:
        input_val = st.number_input("", min_value=0, max_value=100, value=st.session_state[f"{subject}_score"], key=f"{subject}_input")

    # Update session_state if either changed
    if slider_val != st.session_state[f"{subject}_score"]:
        st.session_state[f"{subject}_score"] = slider_val
    elif input_val != st.session_state[f"{subject}_score"]:
        st.session_state[f"{subject}_score"] = input_val

    return st.session_state[f"{subject}_score"]

# Get scores
math = get_synced_score("Math")
reading = get_synced_score("Reading")
writing = get_synced_score("Writing")

# -------------------------
if st.button("Predict"):
    avg_score = np.mean([math, reading, writing])
    
    if avg_score >= 90:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")


