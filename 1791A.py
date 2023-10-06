res = []
STRING = 'codeforces'
for _ in range(int(input())):

    l = input()

    if l.lower() in STRING:
        res.append("YES")
    else:
        res.append("NO")

print(*res, sep="\n")
