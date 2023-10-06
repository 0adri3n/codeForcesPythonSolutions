res = []

for _ in range(int(input())):
    l = int(input())
    arr1 = [int(i) for i in range(2, l+1, 2) if i%2==0]
    arr2 = [int(i) for i in range(1, l-1, 1) if i%2!=0]
    arr2.append(sum(arr1)-sum(arr2))
    arr = arr1 + arr2
    arr = [str(i) for i in arr]
    
    if int(arr[-1])%2!=0:
        res.append("YES")
        s = " ".join(arr)
        res.append(s)
    else:
        res.append("NO")



print(*res, sep="\n")
    