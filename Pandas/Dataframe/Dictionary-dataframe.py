import pandas as pd

dict = {
    "name" : ["snegha","Krishva", "Kousi", "Sumathi"],
    "age" : [21,1,25,32],
    "language" : ["tamil","English","Tamil","Tamil"]
}
result = pd.DataFrame(dict)
print(result)

# Loc - return one or more specified rows
print("Using specified rows", result.loc[0])

print("Using specified rows", result.loc[[0,1]])