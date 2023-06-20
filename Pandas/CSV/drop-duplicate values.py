import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data.drop_duplicates(subset = "age", keep = False, inplace = True)
print(result)