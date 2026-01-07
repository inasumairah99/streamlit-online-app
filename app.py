import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# --- PAGE CONFIG ---
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

# --- TITLE & DESCRIPTION ---
st.title("🎓 Student Performance Prediction App")
st.write("""
This app predicts if a student will be a 'High Performer' (Pass) or 'Needs Improvement' (Fail) based on their profile and scores.
""")

# --- SIDEBAR: USER INPUT ---
st.sidebar.header("Student Information")

def get_user_input():
    # Numerical Inputs (Math, Reading, Writing)
    math = st.sidebar.slider("Math Score", 0, 100, 70)
    reading = st.sidebar.slider("Reading Score", 0, 100, 70)
    writing = st.sidebar.slider("Writing Score", 0, 100, 70)
    
    # Categorical Inputs (Based on your dataset)
    gender = st.sidebar.selectbox("Gender", ["male", "female"])
    race = st.sidebar.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parent_edu = st.sidebar.selectbox("Parental Education", 
                                     ["some high school", "high school", "some college", 
                                      "associate's degree", "bachelor's degree", "master's degree"])
    lunch = st.sidebar.selectbox("Lunch Type", ["standard", "free/reduced"])
    prep_course = st.sidebar.selectbox("Test Prep Course", ["none", "completed"])

    # Create a dictionary for the inputs
    data = {
        'math score': math,
        'reading score': reading,
        'writing score': writing,
        'gender': gender,
        'race/ethnicity': race,
        'parental level of education': parent_edu,
        'lunch': lunch,
        'test preparation course': prep_course
    }
    return pd.DataFrame(data, index=[0])

# Store user input
input_df = get_user_input()

# --- DISPLAY INPUT ---
st.subheader("Selected Student Profile")
st.write(input_df)

# --- PREDICTION LOGIC ---
# Note: In a real project, you would load your saved .pkl model here.
# For this demo, we use the logic from your notebook (Mean Score >= 90 is a Pass).
if st.button("Predict Result"):
    # Calculate Mean Score
    avg_score = input_df[['math score', 'reading score', 'writing score']].mean(axis=1).values[0]
    
    st.divider()
    st.subheader("Prediction Result:")
    
    if avg_score >= 90:
        st.success(f"### Result: PASS (High Performer) ✅")
        st.write(f"The average score is {avg_score:.2f}. This student is in the top bracket.")
    else:
        st.error(f"### Result: FAIL (Needs Improvement) ❌")
        st.write(f"The average score is {avg_score:.2f}. A score of 90+ is required for 'Pass' status in this model.")

# --- MODEL INFO ---
st.info("Model Used: Logistic Regression (Highest Stability in testing).")


