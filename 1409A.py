from math import ceil
res = []
for _ in range(int(input())):
    
    a, b = input().split()
    a, b = int(a), int(b)
    m = max(a, b)
    mi = min(a, b)

    s1 = m - mi
    s1/=10

    s1 = ceil(s1)

    res.append(s1)

print(*res, sep="\n")
    
