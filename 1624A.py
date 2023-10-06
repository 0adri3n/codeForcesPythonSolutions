res = []

for _ in range(int(input())):

    _len = int(input())

    n = [int(i) for i in input().split()]

    res.append(max(n) - min(n))

print(*res, sep="\n")