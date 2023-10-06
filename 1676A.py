res = []
for _ in range(int(input())):
    n = input()
    s1 = 0
    s2 = 0
    for i in n[3:]:
        s1+=int(i)
    for i in n[:3]:
        s2+=int(i)
    if s1 == s2:
        res.append("YES")
    else:
        res.append("NO")
print(*res, sep="\n") 