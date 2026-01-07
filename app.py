import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 1. Page Configuration
st.set_page_config(page_title="Student Performance (Logistic Regression)", layout="centered")

# 2. Load the cleaned and encoded data
@st.cache_data
def load_data():
    # Load the dataset you saved after cell 2/3
    return pd.read_csv("StudentsPerformance_final_encoded.csv")

df = load_data()

# 3. Model & Scaler Preparation
@st.cache_resource
def setup_model(data):
    # Separate Features and Target
    X = data.drop(columns=['Pass/Fail'])
    y = data['Pass/Fail']
    
    # Logistic Regression requires scaling for better performance
    scaler = StandardScaler()
    numerical_cols = ['math score', 'reading score', 'writing score']
    
    X_scaled = X.copy()
    X_scaled[numerical_cols] = scaler.fit_transform(X[numerical_cols])
    
    # Train Logistic Regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_scaled, y)
    
    return model, scaler, X.columns

model, scaler, model_columns = setup_model(df)

# 4. Streamlit GUI Layout
st.title("📊 Student Performance Predictor")
st.subheader("Model: Logistic Regression")

with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        math = st.number_input("Math Score", 0, 100, 70)
        reading = st.number_input("Reading Score", 0, 100, 70)
        writing = st.number_input("Writing Score", 0, 100, 70)
    
    with col2:
        gender = st.selectbox("Gender", ["female", "male"])
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
        prep = st.selectbox("Test Prep Course", ["none", "completed"])
        # Add other categories based on your dataset columns
        race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])

    submit = st.form_submit_button("Analyze Student")

# 5. Prediction Logic
if submit:
    # Create a DataFrame for the single input row
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fill Numerical Values
    input_df['math score'] = math
    input_df['reading score'] = reading
    input_df['writing score'] = writing
    
    # Apply Scaling to numerical values (using the saved scaler)
    input_df[['math score', 'reading score', 'writing score']] = scaler.transform(
        input_df[['math score', 'reading score', 'writing score']]
    )
    
    # Fill One-Hot Encoded Values
    if gender == "male": input_df['gender_male'] = 1
    if lunch == "standard": input_df['lunch_standard'] = 1
    if prep == "none": input_df['test preparation course_none'] = 1
    if race != "group A": input_df[f"race/ethnicity_{race}"] = 1
    
    # Predict Probability and Class
    prob = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    
    # 6. Display Results
    st.divider()
    if prediction == 1:
        st.success(f"### Prediction: PASS (90+ Avg)")
        st.metric("Pass Probability", f"{prob:.2%}")
    else:
        st.error(f"### Prediction: FAIL (< 90 Avg)")
        st.metric("Pass Probability", f"{prob:.2%}")
