import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data.replace(to_replace="n.a", value=23)
print(result.to_string())