import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data.rename(columns = {
    "name" : "Name",
    "nationality" : "Nationality"
})
print(result)