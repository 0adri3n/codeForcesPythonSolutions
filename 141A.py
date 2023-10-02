gn = input()
nr = input()
l = input()

lList = list(l)
nameList = list(gn) + list(nr)
if sorted(lList) == sorted(nameList):
    print("YES")
else:
    print("NO")