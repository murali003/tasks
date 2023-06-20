import pandas as pd

data = pd.read_csv("student-dataset.csv", index_col = "name")
result = data.aggregate({"age" : ['min', 'max'],
                         "math.grade" : ['sum','min','max'],
                         "coverletter.rating" : ['sum','min']
})
print(result)