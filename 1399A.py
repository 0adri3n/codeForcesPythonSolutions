# 1399A
res = []
for _ in range(int(input())):
    _len = int(input())
    l = [int(i) for i in input().split(" ")]
    if _len>1:
        # ai = 0
        # aj = len(l)-1
        # while abs(l[ai]-l[aj]) <= 1:
            
            # if abs(l[ai]-l[aj]) <= 1:
                # mini = min(l[ai], l[aj])
                # if mini == l[ai]: aj-=1
                # else: ai+=1
                # l.remove(mini)
            
            # if aj==ai:
                # break
            
        l = sorted(l)
        bad = False
        for i in range(len(l)-1):
            print(l[i])
            print(l[i]+1>l[i+1])
            if l[i]+1<l[i+1]:
                bad = True
                break

        if bad:
            res.append("NO")
        else:
            res.append("YES")
    
    elif all(element == l[0] for element in l) or _len == 1:
        
        res.append("YES")
        
    
print(*res, sep="\n")