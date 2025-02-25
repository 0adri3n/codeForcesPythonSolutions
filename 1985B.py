r = []

for _ in range(int(input())) :

    n = int(input())
    x = 1
    maxi = 0
    maxi_x = 0
    
    for i in range(n) :

        s = 0
        counter = 1
        kp = True

        while kp :

            if x*counter > n :
                kp = False
            else :
                s += x*counter
                counter += 1
        
        if s > maxi and i != 0: 
            maxi = s
            maxi_x = x

        x += 1
    
    r.append(str(maxi_x))

print("\n".join(r))