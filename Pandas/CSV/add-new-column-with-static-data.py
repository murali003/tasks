import pandas as pd

data = pd.read_csv("student-dataset.csv")
data["Marks"] = "12"
print(data.to_string())