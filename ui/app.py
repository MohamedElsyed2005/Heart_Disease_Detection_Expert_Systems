import streamlit as st

st.title("Heart Disease Detection System")


st.write("""
This application predicts the risk of heart disease based on the health indicators you input.
""")

# User input 
age = st.slider("Age", 20, 100, 30)
blood_pressure = st.slider("Blood Pressure (mmHg)", 80, 200, 120)
cholesterol = st.slider("Cholesterol (mg/dL)", 100, 400, 200)
smoking = st.radio("Do you smoke?", ("Yes", "No"))
exercise = st.radio("Do you exercise regularly?", ("Yes", "No"))

# Button for prediction
if st.button("Predict Risk"):
# المفروض ندخلها في test 
# ونحط تحت الشرط اللوجيك اللي طلع بعد تعليم الداتا ماشي يا فوزي انت وهو 
    # Display the result
    st.success(f"Prediction Result: {risk}")