res = []
for _ in range(int(input())):

        n = [int(i) for i in input().split()]

        m = max(n)
        n.remove(m)

        if m == n[0] + n[-1]:
            res.append("YES")
        else:
            res.append("NO")
print(*res, sep="\n")