n = int(input())
r = []
for _ in range(n) :

    ln = int(input())

    lines = input().split(" ")
    lines = [int(i) for i in lines]


    if len(lines) == 1:

        r.append("YES")

    else :

        if len(set(lines)) == len(lines) :

            r.append("YES")

        else :

            r.append("NO")
        
print("\n".join(r))

