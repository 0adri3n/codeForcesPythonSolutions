res = []
for _ in range(int(input())):

    _len = int(input())
    arr = [int(i) for i in input().split()]



    o = 0
    e = 0

    for i in range(len(arr)):

        if i%2!=arr[i]%2:

            if arr[i]%2==1:

                o+=1
            
            else:

                e+=1

    if o == e:

        res.append(o)

    else:
        res.append(-1)

print(*res, sep="\n")