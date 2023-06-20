import pandas as pd

result = pd.read_csv('student-dataset.csv')
print(result.sort_values(by=['name','nationality'],ascending = [True, False]))