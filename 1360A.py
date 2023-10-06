res = []

for _ in range(int(input())):

    a, b = input().split()
    a, b = int(a), int(b)

    mi = min(a, b)
    ma = max(a, b)

    mi = 2*mi
    if ma<mi:
        ma += abs(mi-ma)
    else:
        mi += abs(mi-ma)

    res.append(mi*ma)

print(*res, sep="\n")