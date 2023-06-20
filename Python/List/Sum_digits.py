list = [1,23,42,45]
print("original list", list)
result=[]
for elements in list:
    sum =0
    for digits in str(elements):
        sum += int(digits)
    result.append(sum)

print("list after suming", result)