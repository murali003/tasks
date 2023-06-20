import pandas as pd
import numpy as np

nums = {'Car Model Number': [223, np.nan, 237, 195, np.nan,
                             575, 110, 313, np.nan, 190, 143,
                             np.nan],
        'Engine Number': [4511, np.nan, 7570, 1565, 1450, 3786,
                          2995, 5345, 7777, 2323, 2785, 1120]}

df = pd.DataFrame(nums, columns=['Car Model Number'])

df['Car Model Number'] = df['Car Model Number'].replace(np.nan, 0)
print(df)