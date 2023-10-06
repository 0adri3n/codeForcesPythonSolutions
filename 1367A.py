res = []
for _ in range(int(input())):
    s = list(input())
    st = ""
    i=0
    while i<len(s)-1:
        if s[i] == s[i+1]:
            st+=s[i]
            i+=2
        else:
            st+=s[i]
            i+=1
    st+=s[-1]
    res.append(st)
print(*res, sep="\n")