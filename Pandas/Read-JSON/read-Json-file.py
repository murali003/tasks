import pandas as pd

result = pd.read_json("student-json.json")
print(result.to_string())