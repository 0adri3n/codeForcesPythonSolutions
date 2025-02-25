r = []

for _ in range(int(input())) :

    ln = int(input())

    f_line = input()
    s_line = input()

    f_line = f_line.replace("G", "B")
    s_line = s_line.replace("G", "B")

    identical = True

    for ele in range(ln) :

        if f_line[ele] != s_line[ele] :

            identical = False

    if identical : 

        r.append("YES")
    
    else :

        r.append("NO")


print("\n".join(r))
