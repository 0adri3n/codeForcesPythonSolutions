res = []

for _ in range(int(input())):

    s = input()

    l = int(len(s)/2)

    if s[l:] == s[:l]:
        res.append("YES")
    else:
        res.append("NO")

print(*res, sep="\n")