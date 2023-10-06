res = []
from math import floor
for _ in range(int(input())):

    n = int(input())
    a = floor(n/3)
    b = (n-a)//2
    if a+b*2!=n:
        a+=1
    res.append(str(a) + " " + str(b))

print(*res, sep="\n")
