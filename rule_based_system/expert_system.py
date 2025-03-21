engine=Heart_Expert()
engine.reset()
Patient = EXPERT_DATA.iloc[1].to_dict()
print(Patient)

for key, value in Patient.items():
    engine.declare(Fact(**{key: value}))


engine.run()