import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import joblib

df = pd.read_csv(r"..\data\heart.csv")

X = df.drop(columns=['target'])
y = df['target']

# Define parameter distribution for hyperparameter tuning
param_dist = {
    'max_depth': randint(3, 20),  # Random values between 3 and 20
    'min_samples_split': randint(2, 15)  # Random values between 2 and 15
}

# Initialize Decision Tree Classifier
tree_clf = DecisionTreeClassifier(random_state=42)

# Perform Randomized Search for best hyperparameters
random_search = RandomizedSearchCV(tree_clf, param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)
random_search.fit(X, y)

# Train the best model
best_model = random_search.best_estimator_

# Save the best model
joblib.dump(best_model, "decision_tree_model.pkl")