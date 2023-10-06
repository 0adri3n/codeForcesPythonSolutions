res = []
nb = []
for _ in range(int(input())):
    n = int(input())
    nb.append(n)

poly = []

i=1
while i<1667:
    if i%3 != 0 and i%10 != 3:
        poly.append(i)
    i+=1

for i in nb:
    print(poly[i-1])