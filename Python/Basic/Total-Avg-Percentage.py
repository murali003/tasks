tamil = float(input("Enter tamil marks ::"))
english = float(input("Enter english marks ::"))
maths = float(input("Enter maths marks ::"))
science = float(input("Enter science marks ::"))
social = float(input("Enter social marks ::"))

total = tamil+english+maths+science+social
average = total/5
percentage = (total/500)*100

print("Total marks = ", total)
print("Average  = ", average)
print("Percentage  = ", percentage)