string = input("Please enter any String : ")
words = []

words = string.split()
myDict = {}
for key in words:
    myDict[key] = words.count(key)

print(myDict)