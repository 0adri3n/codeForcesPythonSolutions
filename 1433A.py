res = []
for _ in range(int(input())):

    inp = input()

    st = ""
    s=0
    i=1
    y=1

    while st!=inp:
        if len(st)>3:
            i+=1
            y=1
            st=""
        st=str(i)*y
        s+=y
        y+=1

    res.append(s)

print(*res, sep="\n")