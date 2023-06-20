set = {23,53,33,22,12,76}

evensum = 0
oddsum = 0

for i in set :
    if(i %2 == 0):
        evensum += i
    else:
        oddsum += i
print("sum of even numbers", evensum)
print("sum of odd numbers", oddsum)
