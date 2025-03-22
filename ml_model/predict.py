import pandas as pd 
import joblib
from sklearn.metrics import classification_report

model = joblib.load("decision_tree_model.pkl")
test_data = pd.read_csv(r"../data/test_cleaned.csv")
X_test = test_data.drop(columns=['target'])
y_test = test_data['target']
prediction = model.predict(X_test)
clf_report = classification_report(y_test, prediction)
print(clf_report)