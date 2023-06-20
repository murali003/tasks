import pandas as pd

data = pd.read_csv("student-dataset.csv", index_col= "name")
result = data.iloc[:,[0,1,2,3]]
print(result)