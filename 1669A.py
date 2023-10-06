res = []
for _ in range(int(input())):

    t = int(input())

    if t<=1399:
        res.append("Division 4")
    elif 1400<=t<=1599:
        res.append("Division 3")
    elif 1600<=t<=1899:
        res.append("Division 2")
    elif t>=1900:
        res.append("Division 1")
print(*res, sep="\n")