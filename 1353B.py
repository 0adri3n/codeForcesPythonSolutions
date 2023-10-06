res = []

for _ in range(int(input())):

    n, k = input().split()
    n, k = int(n), int(k)
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    a = sorted(a)
    b = sorted(b, reverse=True)


    for j in range(k):
        t = a[j]
        if a[j]<b[j]:
            a[j] = b[j]
            b[j] = t
        
    res.append(sum(a))
    



print(*res, sep="\n")