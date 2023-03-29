n = int(input())
combin = []
for i in range(n):
    line = list(map(int, input().split()))
    combin.append(line)

for line in combin:

    print((line[1]-line[0]%line[1])%line[1])