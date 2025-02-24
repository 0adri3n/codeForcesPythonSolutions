res = []

for _ in range(int(input())) :

    l = int(input())
    array = [int(i) for i in input().split(" ")]

    no_dup = list(dict.fromkeys(array))
    if len(no_dup) == 1 :
        res.append(0)

    else :

        s = 0
        min_c = min(array)
        for c in array :
            
            s += c - min_c
        
        res.append(s)
    
for r in res :
    print(r)