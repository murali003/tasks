import pandas as pd

result = pd.read_json("student-json.json")
result.to_csv("student.csv")
data = pd.read_csv("student.csv")
print(data.to_string)