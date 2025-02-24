n = int(input())
r = []
for _ in range(n) :

    ln = int(input())

    lines = input().split(" ")
    str_l = "".join(lines).split("1")
    
    maxlen = 0

    for ele in str_l :

        if len(ele) > maxlen :

            maxlen = len(ele)

    r.append(str(maxlen))

print("\n".join(r))