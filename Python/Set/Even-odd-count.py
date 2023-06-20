set = {23,53,33,22,12,76}

evencount = 0
oddcount = 0

for i in set :
    if(i %2 == 0):
        evencount += 1
    else:
        oddcount += 1
print("count of even numbers", evencount)
print("count of odd numbers", oddcount)
