res = []
for _ in range(int(input())):
    p = [int(i) for i in input().split()]
    t = p[0]
    c = 0
    for i in range(1, len(p)):
        if p[i] > t:
            c+=1
    res.append(c)
print(*res, sep="\n")