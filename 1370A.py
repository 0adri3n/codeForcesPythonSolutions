res = []
from math import floor
for _ in range(int(input())):
    n = int(input())
    res.append(floor(n/2))
print(*res, sep="\n")
