list = [4,5,6,1,4,6,8]
final = []
for i in list:
    if i not in final:
        final.append(i)
print("final list without duplicate::", final)