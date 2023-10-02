res = []
for _ in range(int(input())):

    _len = int(input())
    n = [int(i) for i in input().split()]

    l1 = [n[0]]
    l2 = []

    for i in range(1, len(n)):

        if n[i] == l1[0]:
            l1.append(n[i])
        else:
            l2.append(n[i])
    
    if len(l1)<len(l2):
        res.append(n.index(l1[0])+1)
    else:
        res.append(n.index(l2[0])+1)

print(*res, sep="\n")

