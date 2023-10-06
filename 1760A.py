res = []

from statistics import median

for _ in range(int(input())):

    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    res.append(median([a, b, c]))

print(*res, sep="\n")