sum = 0
print("Enter 10 numbers")
for i in range(1,11):
    number = int(input("Number %d =" %i))
    sum = sum + number
average = sum/10
print("The sum of 10 numbers ::", sum)
print("The average of 10 numbers ::", average)