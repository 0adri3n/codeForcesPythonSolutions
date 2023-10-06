res = []
import itertools
for _ in range(int(input())):

    _len = int(input())
    l = [int(i) for i in input().split()]

    groups = itertools.groupby(l)
    if sum(l)%2 == 0:
        if len(list(groups)) == 1:
            if len(l)%2==0:
                res.append("YES")
            else:
                res.append("NO")
        else:
            res.append("YES")
    else:
        res.append("NO")

print(*res, sep="\n")