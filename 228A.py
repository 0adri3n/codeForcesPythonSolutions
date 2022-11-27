s=input().split()
dict={}
for n in s:
    if n not in dict.keys():
        dict.update({n: s.count(n)})
som=0
for i in dict.values():
    if i>1:
        if i>2:
            som+=i-1
        else:som+=1
print(som)
