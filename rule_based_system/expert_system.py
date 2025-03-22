from rules import Heart_Expert
from experta import Fact
import pandas as pd

engine = Heart_Expert()
engine.reset()

test = pd.read_csv(r"..\data\heart.csv")

test_1_dict = test.iloc[:1].to_dict(orient="records")[0]

# Declare patient facts
for key, value in test_1_dict.items():
    engine.declare(Fact(**{key: value}))

final = engine.run()