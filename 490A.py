_len = int(input())
c = [int(i) for i in input().split()]
sortedc = sorted(c)
t = {"l": []}
ind = {1: [], 2: [], 3: []}

for i in range(len(c)):
    if c[i] == 1:
        ind[1].append(i+1)
    elif c[i] == 2:
        ind[2].append(i+1)
    elif c[i] == 3:
        ind[3].append(i+1)

if len(ind[1]) == 0 or len(ind[2]) == 0 or len(ind[3]) == 0:
    print("0")
else:
    while len(ind[1]) > 0 and len(ind[2]) > 0 and len(ind[3]) > 0:
        un = ind[1].pop(0)
        deux = ind[2].pop(0)
        trois = ind[3].pop(0)
        temp = [un, deux, trois]
        t["l"].append(temp)
    print(len(t["l"]))
    for li in t["l"]:
        print(*li, sep=" ")