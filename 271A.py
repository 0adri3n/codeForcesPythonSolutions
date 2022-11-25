year=input()

def checkDist(year):
    count={}
    for i in range(len(year)):
        if year[i] not in count.keys():
            c=year.count(year[i])
            count.update({year[i]: c})
    diff=False
    for i in count.values():
        if i>1:
            diff=True
    return diff
year=str(int(year)+1)
while checkDist(year):
    year=str(int(year)+1)
print(year)
