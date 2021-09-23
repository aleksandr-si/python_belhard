array = [1,2,33,44,43,7,77,10,14]
result=[]
for i,x in enumerate(array):
    if x % 7 == 0:
        result.append((x,i))

print(result)
    