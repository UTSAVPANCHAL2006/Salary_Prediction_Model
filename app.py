import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("data/Salary_Data.csv")

model = joblib.load("src/RF_Salary_pred.pkl")
scaler = joblib.load("src/scaler.pkl")
expected_columns = joblib.load("src/columns.pkl")


st.title("💸 Salary Prediction")
st.markdown("Provide the following details to predict your monthly salary:")

age = st.number_input("Age", min_value=18, max_value=100, value=25)
experience = st.number_input("Years of Experience", min_value=0, max_value=80, value=1)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor", "Master", "PhD"])
job_title = st.selectbox("Select Job Title", df['Job Title'].unique().tolist())


def encode_gender(g):
    return {"Male": 1, "Female": 0}.get(g, 1)

def encode_education(e):
    return {"Bachelor": 1, "Master": 2, "PhD": 3}.get(e, 0)

def encode_job_title(title):
    titles = df['Job Title'].unique().tolist()
    return titles.index(title) if title in titles else 0  # Better fallback

if st.button("Predict Salary"):
    # Scale age and experience together
    scaled = scaler.transform([[age, experience]])
    age_scaled = scaled[0][0]
    experience_scaled = scaled[0][1]

    input_dict = {
        "Age_scaled": age_scaled,
        "Years of Experience_scaled": experience_scaled,
        "Gender_Encode": encode_gender(gender),
        "Education Level_Encode": encode_education(education),
        "Job Title_Encode": encode_job_title(job_title)
    }

    X_input = pd.DataFrame([input_dict], columns=expected_columns)
    prediction = model.predict(X_input)[0]
    st.success(f"Predicted Salary: ₹{prediction:,.2f}")
