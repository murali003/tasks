import pandas as pd
dataFrame1 = pd.DataFrame(
   {
      "Car": ['BMW', 'Lexus', 'Audi', 'Mustang', 'Bentley', 'Jaguar'],"Units": [100, 150, 110, 80, 110, 90]
   }
)
dataFrame2 = pd.DataFrame(
   {
      "Car": ['BMW', 'Lexus', 'Audi', 'Mustang', 'Mercedes', 'Jaguar'],"Reg_Price": [7000, 1500, 5000, 8000, 9000, 6000]

   }
)
mergedRes = pd.merge(dataFrame1, dataFrame2, on ='Car')
print(mergedRes)