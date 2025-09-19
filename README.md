# Heart Disease Prediction App

This project is a **Streamlit web application** that predicts the likelihood of heart disease based on user-provided health parameters. The model uses a **K-Nearest Neighbors (KNN)** classifier trained on a heart disease dataset.  

## Features
- Interactive UI built with Streamlit  
- User inputs medical attributes such as age, chest pain type, cholesterol, etc.  
- Transforms input data using a pre-trained **scaler**  
- Predicts heart disease chances using the saved **KNN model**  
- Displays results with clear **success/error messages**  

## Files
- **app.py** → The Streamlit application script (your main code).  
- **KNN_heart.pkl** → Trained KNN model file saved with `joblib`.  
- **scaler.pkl** → Fitted data scaler for preprocessing user inputs.  
- **columns.pkl** → Column list ensuring feature alignment with model training.  

## Installation
1. Clone the repository or copy the project files.  
2. Install required dependencies:  

```bash
pip install streamlit pandas scikit-learn joblib
```

3. Ensure the following files are in the project directory:  
   - `app.py`  
   - `KNN_heart.pkl`  
   - `scaler.pkl`  
   - `columns.pkl`  

## Usage
Run the Streamlit app with:

```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually http://localhost:8501) in your browser.  

## User Inputs
- **Age**: Patient’s age (18–100 years)  
- **Sex**: Male (M) or Female (F)  
- **Chest Pain Type**: Typical Angina (TA), Atypical Angina (ATA), Non-anginal Pain (NAP), Asymptomatic (ASY)  
- **Resting Blood Pressure**: mm Hg (80–200)  
- **Cholesterol**: mg/dl (100–600)  
- **Fasting Blood Sugar**: >120 mg/dl (0 = No, 1 = Yes)  
- **Resting ECG**: Normal, ST abnormalities, LVH  
- **Max Heart Rate**: Achieved heart rate (60–220 bpm)  
- **Exercise Induced Angina**: Yes (Y), No (N)  
- **Oldpeak**: ST depression (0.0–6.0)  
- **ST Slope**: Up, Flat, Down  

## Output
- **Positive Prediction (Error Alert)**: "Model predicts that you may have heart disease. Please consult a doctor."  
- **Negative Prediction (Success Message)**: "Model predicts that you are unlikely to have heart disease."  


Would you like me to also include instructions on **how to train the KNN model and generate the .pkl files**, so others can reproduce your setup from scratch?
