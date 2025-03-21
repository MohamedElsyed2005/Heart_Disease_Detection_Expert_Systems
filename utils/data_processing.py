import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

def preprocessing_pipeline(file_path, train_output, test_output):
    
    raw_data = pd.read_csv(file_path)

    numeric_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

    train_data, test_data = train_test_split(raw_data, test_size=0.2, random_state=42)

    num_pipeline = make_pipeline(SimpleImputer(strategy="median"), MinMaxScaler())
    cat_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore"))

    preprocessing = make_column_transformer(
        (num_pipeline, numeric_features),
        (cat_pipeline, categorical_features)
    )

    train_cleaned = preprocessing.fit_transform(train_data)
    test_cleaned = preprocessing.transform(test_data)

    cat_feature_names = preprocessing.named_transformers_['pipeline-2'].named_steps['onehotencoder'].get_feature_names_out(categorical_features)
    all_feature_names = numeric_features + list(cat_feature_names)

    train_cleaned_df = pd.DataFrame(train_cleaned, columns=all_feature_names)
    test_cleaned_df = pd.DataFrame(test_cleaned, columns=all_feature_names)

    train_cleaned_df['target'] = train_data['target'].values
    test_cleaned_df['target'] = test_data['target'].values

    train_cleaned_df.to_csv(train_output, index=False, encoding="utf-8")
    test_cleaned_df.to_csv(test_output, index=False, encoding="utf-8")

if __name__ == "__main__":
    preprocessing_pipeline("..//data//heart.csv", "..//data//train_cleaned.csv", "..//data//test_cleaned.csv")
