import pandas as pd
data = pd.Series([1,2,3,4,5])
result = data.apply(lambda x: x/2)
print(result)
