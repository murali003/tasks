import pandas as pd

data = pd.read_csv("student-dataset.csv", index_col  ="name")
result = data["nationality"]
print(result)