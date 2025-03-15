import numpy as np 
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import make_pipeline

data = pd.read_csv(r"..\data\heart.csv")

columns = data.columns

num_pipeline = make_pipeline(SimpleImputer(strategy = "median"),
                             MinMaxScaler())

cat_pipeline = make_pipeline(SimpleImputer(strategy = "most_frequent"),
                             OneHotEncoder(handle_unknown = "ignore"))

preprocessing = make_column_transformer(
        (num_pipeline, make_column_selector(dtype_include = np.number)),
        (cat_pipeline, make_column_selector(dtype_include = object))
        )

data_cleaned = preprocessing.fit_transform(data)
data_cleaned = pd.DataFrame(data_cleaned, columns = columns)
data_cleaned.to_csv(r"../data/cleaned_data.csv", index=False, encoding="utf-8")
