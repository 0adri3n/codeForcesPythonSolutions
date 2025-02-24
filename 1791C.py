n = int(input())
r = []
for _ in range(n) :

    ln = int(input())

    bina = list(input())

    c = len(bina)


    i_s = 0
    i_e = -1

    kp = True

    while kp : 

        if c == 0 :

            kp = False

        elif bina[i_s] != bina[i_e]:

            i_s += 1
            i_e -= 1

            c -= 2

        else :

            kp = False

    r.append(str(c))

        
print("\n".join(r))

