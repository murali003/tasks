dic1 = {'name' : 'snegha' , 'age' : 21}
dic2 = {'language' : 'tamil'}

dic3 = dic1 | dic2
print(dic3)

print({**dic1, **dic2})

dic3 = dic1.copy()
dic3.update(dic2)
print(dic3)