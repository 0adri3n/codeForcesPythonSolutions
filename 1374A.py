res = []

for _ in range(int(input())):

    x, y, n = input().split()
    x, y, n = int(x), int(y), int(n)

    z = n%x
    if z>y:
        res.append(n-(z-y))
    elif z==y:
        res.append(n)
    else:
        res.append((n-x)+(y-z))
    
print(*res, sep="\n")