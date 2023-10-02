res = []
for i in range(int(input())):
    n = input()
    if n.lower() == "yes":
        res.append("YES")
    else:
        res.append("NO")
print(*res, sep="\n")
