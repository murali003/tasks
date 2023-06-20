import pandas as pd

data = pd.read_csv("student-dataset.csv", index_col="name")
result = data.iloc[[18, 21]]
print(result)