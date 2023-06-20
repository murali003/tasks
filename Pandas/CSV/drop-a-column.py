import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data.drop(['city'], axis = 1)
print(result.to_string())