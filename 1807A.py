res = []

for _ in range(int(input())):

    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    if a+b==c:
        res.append("+")
    else:
        res.append("-")

print(*res, sep="\n")