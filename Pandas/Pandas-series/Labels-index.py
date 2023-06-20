import pandas as pd

series1 = [1,2,3]
result = pd.Series(series1, index = ['X', 'Y', 'Z'])
print(result)

print("The result based on index ::", result['Y'])