import pandas as pd

data = pd.read_csv("student-dataset.csv", index_col = "name")
result = data.loc["Brooke Cazares"]
print(result)