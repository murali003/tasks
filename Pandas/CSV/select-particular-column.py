import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data['nationality']
print(result)