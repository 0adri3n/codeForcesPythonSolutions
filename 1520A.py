res = []

for _ in range(int(input())):

    _len = int(input())
    s = []
    t = input()
    b = False
    prev = ""
    for i in t:
        if i not in s:
            s.append(i)
        elif i in s and i!=prev:
            b = True
        prev = i
    
    if b:
        res.append("NO")
    else:
        res.append("YES")

print(*res, sep="\n")