nbone=input()
nbtwo=input()
res=""
for i in range(len(nbone)):
    if nbone[i]!=nbtwo[i]:res+="1"
    else:res+="0"
print(res)
