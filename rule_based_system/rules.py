from experta import KnowledgeEngine, Rule, Fact, P


class Heart_Expert(KnowledgeEngine):
    
    @Rule(Fact(trestbps=P(lambda x: x > 140)))
    def high_blood_pressure(self):
        print("Warning: High Blood Pressure (trestbps > 140) -> Potentially Harmful to the Heart <Low Effect>")

    @Rule(Fact(chol=P(lambda x: x > 200)))  
    def high_cholesterol(self):
        print("Warning: High Cholesterol (chol > 200) -> Potentially Harmful to the Heart <Low Effect>")

    @Rule(Fact(thalach=P(lambda x: x < 120)))
    def low_heart_rate(self):
        print("Warning: Low Heart Rate (thalach < 120) -> Bad Heart Functionality <High Effect>")

    @Rule(Fact(fbs=P(lambda x: x > 120)))  
    def high_fbs(self):
        print("Warning: High Fasting Blood Sugar (fbs > 120) -> Potentially Harmful to the Heart <Low Effect>")

    @Rule(Fact(oldpeak=P(lambda x: x > 1)))
    def high_oldpeak(self):
        print("Warning: High Oldpeak (oldpeak > 1) -> Bad Heart Functionality <High Effect>")

    @Rule(Fact(ca=P(lambda x: x > 2)))  
    def high_ca(self):
        print("Warning: High Calcium Score (ca > 2) -> Bad Heart Functionality <Mid-Normal Effect>")

    @Rule(Fact(cp=P(lambda x: x == 3)))
    def high_cp(self):
        print("Warning: Chest Pain Type 3 (cp == 3) -> Bad Heart Functionality <High Effect>")

    @Rule(Fact(exang=P(lambda x: x == 1)))
    def exercise_angina(self):
        print("Warning: Exercise-Induced Angina Detected (exang == 1) -> Bad Heart Functionality <High Effect>")

    
    @Rule(Fact(exang=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def exang_oldpeak_high_risk(self):
        print("High Warning!!: Combination of Exercise-Induced Angina & High Oldpeak -> Consult a Doctor!!")

    @Rule(Fact(thalach=P(lambda x: x < 120)), Fact(cp=P(lambda x: x == 3)))
    def thalach_cp_high_risk(self):
        print("High Warning!!: Low Heart Rate & Chest Pain Type 3 -> Consult a Doctor!!")

    @Rule(Fact(thalach=P(lambda x: x < 120)), Fact(cp=P(lambda x: x == 3)), 
          Fact(exang=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def multiple_risk_factors(self):
        print("Critical Warning!!: Multiple High-Risk Factors Detected (oldpeak, exang, thalach, cp) -> Urgent Medical Attention Required!!")

    @Rule(Fact(slope=P(lambda x: x == 1)), Fact(oldpeak=P(lambda x: x > 1)))
    def slope_oldpeak_high_risk(self):
        print("Warning: Flat Slope & High Oldpeak -> Increased Risk of Heart Disease")

    @Rule(Fact(target=1))
    def heart_disease(self):
        print("Diagnosis: This Patient Has Heart Disease")

    @Rule(Fact(target=0))
    def no_heart_disease(self):
        print("Diagnosis: This Patient Does Not Have Heart Disease")

