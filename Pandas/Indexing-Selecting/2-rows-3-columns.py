import pandas as pd
data = pd.read_csv("student-dataset.csv", index_col = "name")
result = data.iloc[[3,5],[0,1,2]]
print(result)