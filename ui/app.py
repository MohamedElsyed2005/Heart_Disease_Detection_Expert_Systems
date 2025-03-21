import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

model_path = os.path.abspath("ml_model/decision_tree_model.pkl")
model = joblib.load(model_path)

scaler_path = os.path.abspath("utils/preprocessing_pipeline.pkl")
scaler = joblib.load(scaler_path)  # preprocessing pipeline

feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']


st.title("Heart disease")


user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(f"Enter the value of {feature}:", min_value=0.0, step=0.1)

user_df = pd.DataFrame([user_input])

user_df_scaled = scaler.transform(user_df)


if st.button("predict"):
    prediction = model.predict(user_df_scaled)  
    result = "Disease heart : " if prediction[0] == 1 else "✅ Good"
    st.subheader(f"Result: {result}")
