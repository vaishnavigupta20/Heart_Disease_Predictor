import streamlit as st
import pandas as pd
import joblib

model = joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart Disease Prediction App")
st.markdown("Provide the following details to predict the presence of heart disease.")

age = st.slider("Age", 18, 100, 35)
sex = st.selectbox("SEX", ['M', 'F'])
chest_pain_type = st.selectbox("Chest Pain Type", ['TA', 'ATA', 'NAP', 'ASY'])
resting_bp = st.number_input("Resting Blood Pressure (in mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (in mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
max_hr = st.slider("Max Heart Rate Achieved", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ['Y', 'N'])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("Predict"):
    raw_data = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain_type: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }
    input_data = pd.DataFrame([raw_data])

    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[expected_columns]
    input_data[expected_columns] = scaler.transform(input_data[expected_columns])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("The model predicts that you may have heart disease. Please consult a doctor.")
    else:
        st.success("The model predicts that you are unlikely to have heart disease.")