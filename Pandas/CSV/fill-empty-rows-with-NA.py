import numpy as np
import pandas as pd

data = pd.read_csv("student-dataset.csv")
result = data.replace(r'^\s*$',np.NAN, regex= True)
print(result)