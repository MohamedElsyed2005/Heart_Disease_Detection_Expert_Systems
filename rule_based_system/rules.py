import sys
sys.path.insert(0, "./ui")
from experta import KnowledgeEngine, Rule, Fact, P

class Heart_Expert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.messages = []  # Store messages to display in Streamlit
    
    @Rule(Fact(trestbps=P(lambda x: x > 140)))
    def high_blood_pressure(self):
        msg = "Warning: High Blood Pressure (trestbps > 140) -> Potentially Harmful to the Heart <Low Effect>"
        self.messages.append(msg)

    @Rule(Fact(chol=P(lambda x: x > 200)))  
    def high_cholesterol(self):
        msg = "Warning: High Cholesterol (chol > 200) -> Potentially Harmful to the Heart <Low Effect>"
        self.messages.append(msg)

    @Rule(Fact(thalach=P(lambda x: x < 120)))
    def low_heart_rate(self):
        msg = "Warning: Low Heart Rate (thalach < 120) -> Bad Heart Functionality <High Effect>"
        self.messages.append(msg)

    @Rule(Fact(fbs=P(lambda x: x > 120)))  
    def high_fbs(self):
        msg = "Warning: High Fasting Blood Sugar (fbs > 120) -> Potentially Harmful to the Heart <Low Effect>"
        self.messages.append(msg)

    @Rule(Fact(oldpeak=P(lambda x: x > 1)))
    def high_oldpeak(self):
        msg = "Warning: High Oldpeak (oldpeak > 1) -> Bad Heart Functionality <High Effect>"
        self.messages.append(msg)

    @Rule(Fact(ca=P(lambda x: x > 2)))  
    def high_ca(self):
        msg = "Warning: High Calcium Score (ca > 2) -> Bad Heart Functionality <Mid-Normal Effect>"
        self.messages.append(msg)

    @Rule(Fact(cp=P(lambda x: x == 3)))
    def high_cp(self):
        msg = "Warning: Chest Pain Type 3 (cp == 3) -> Bad Heart Functionality <High Effect>"
        self.messages.append(msg)

    @Rule(Fact(exang=P(lambda x: x == 1)))
    def exercise_angina(self):
        msg = "Warning: Exercise-Induced Angina Detected (exang == 1) -> Bad Heart Functionality <High Effect>"
        self.messages.append(msg)

    @Rule(Fact(exang=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def exang_oldpeak_high_risk(self):
        msg = "High Warning!!: Combination of Exercise-Induced Angina & High Oldpeak -> Consult a Doctor!!"
        self.messages.append(msg)

    @Rule(Fact(thalach=P(lambda x: x < 120)), Fact(cp=P(lambda x: x == 3)))
    def thalach_cp_high_risk(self):
        msg = "High Warning!!: Low Heart Rate & Chest Pain Type 3 -> Consult a Doctor!!"
        self.messages.append(msg)

    @Rule(Fact(thalach=P(lambda x: x < 120)), Fact(cp=P(lambda x: x == 3)), 
          Fact(exang=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def multiple_risk_factors(self):
        msg = "Critical Warning!!: Multiple High-Risk Factors Detected (oldpeak, exang, thalach, cp) -> Urgent Medical Attention Required!!"
        self.messages.append(msg)

    @Rule(Fact(slope=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def slope_oldpeak_high_risk(self):
        msg = "Warning: Flat Slope & High Oldpeak -> Increased Risk of Heart Disease"
        self.messages.append(msg)

    @Rule(Fact(target=1))
    def heart_disease(self):
        msg = "Diagnosis: This Patient Has Heart Disease"
        self.messages.append(msg)

    @Rule(Fact(target=0))
    def no_heart_disease(self):
        msg = "Diagnosis: This Patient Does Not Have Heart Disease"
        self.messages.append(msg)

