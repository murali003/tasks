import pandas as pd

data = pd.read_csv("student-dataset.csv")
data.to_json("student.json")
result = pd.read_json("student.json")
print(result.to_string())