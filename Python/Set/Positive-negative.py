numbers = {23,-53,33,22,-12,76}

positivecount = 0
negativecount = 0

for i in numbers :
    if(i>0):
        positivecount += 1
    else:
        negativecount += 1
print("count of positive numbers", positivecount)
print("count of negative numbers", negativecount)
