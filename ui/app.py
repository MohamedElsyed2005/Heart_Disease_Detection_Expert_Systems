import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sys
import os
from experta import Fact
from frozendict import frozendict


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rule_based_system.rules import Heart_Expert

model_path = os.path.abspath("ml_model/decision_tree_model.pkl")
model = joblib.load(model_path)

scaler_path = os.path.abspath("utils/preprocessing_pipeline.pkl")
scaler = joblib.load(scaler_path)   # preprocessing pipeline

feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

st.title("Heart Disease Detection System")
st.write("This application predicts the risk of heart disease based on the health indicators you input.")

# User input 
age = st.slider("Age", 20, 100, 30)
sex = st.radio("Gender:", ["Male", "Female"])
cp = st.radio("Type of Chest Pain:", ["No pain", "Typical angina", "Atypical angina", "Non-anginal pain"])
trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 120)
chol = st.slider("Cholesterol (mg/dL)", 100, 400, 200)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dL?", ["Yes", "No"])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.slider("Maximum Heart Rate Achieved", 60, 220, 150)
exang = st.radio("Do you exercise regularly?", ["Yes", "No"])
oldpeak = st.slider("ST Depression Induced by Exercise", 0.0, 6.2, 1.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.slider("Number of Major Vessels (0-4)", 0, 4, 0)
thal = st.selectbox("Thalassemia Type", [0, 1, 2, 3])


sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
exang = 1 if exang == "Yes" else 0


user_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                        exang, oldpeak, slope, ca, thal]], columns=feature_names)

#### streamlit run ui/app.py ----->  paste it in terminal to run 
def predict_decision_tree(data):
    # Normalization with scaler
    ## بالاصح بيحل مشكلة التقسيمة بس برضوا مش فاهم ازاي
    user_data_scaled = scaler.transform(user_data)
    prediction = model.predict(user_data_scaled)
    return prediction


# Button for prediction
if st.button("Predict Using Decision tree"):
    prediction = predict_decision_tree(user_data)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")
    
elif st.button("Predict Using Expert System"):
    engine = Heart_Expert()
    engine.reset()
    
    user_data_dict = user_data.to_dict(orient="records")[0]
    for key, value in user_data_dict.items():
        engine.declare(Fact(**{key: value}))
    
    engine.run()
    
    # Display warnings from the expert system
    if engine.messages:
        for msg in engine.messages:
            st.warning(msg)  # Displays warnings in Streamlit
    else:
        st.success("✅ No significant heart disease risk detected based on rules.")
