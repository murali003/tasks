import pandas as pd

value = 'China'
data = pd.read_csv("student-dataset.csv")
result = data.query("nationality == @value")
print(result.to_string())