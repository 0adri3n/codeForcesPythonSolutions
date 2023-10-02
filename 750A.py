entry = input()
n, k = entry.split(" ")
n, k = int(n), int(k)

pbTime = 0
pbRes = 0
maxTime = (4*60)-k

if n<k:

    i=1
    run = True
    while run:
        if pbTime+(5*i)>maxTime:
            run = False
        else:
            pbTime+= 5*i
            pbRes += 1
            i+=1

    if pbRes>n:
        print(n)
    else:
        print(pbRes)
 
else:
    if n>=10:
        print(n-1)
    else:
        print(n)