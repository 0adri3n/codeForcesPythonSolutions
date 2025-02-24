r = []

for _ in range(int(input())) :

    n, k = input().split(" ")
    n, k = int(n), int(k)
    elements = [int(i) for i in input().split(" ")]

    if k in elements :

        r.append("YES")

    else :

        r.append("NO")

print("\n".join(r))