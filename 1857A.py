res = []

for _ in range(int(input())) :

    l = int(input())
    array = [int(i) for i in input().split(" ")]

    s_e = 0
    s_o = 0

    for i in array :
        if i%2 == 0:
            s_e += i
        else :
            s_o += i
    
    if s_e%2 == 0 and s_o%2 == 0 :
        res.append("YES")
    else :
        res.append("NO")

    
for r in res :
    print(r)