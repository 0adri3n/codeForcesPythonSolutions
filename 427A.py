n = int(input())
c = input()
c = c.split(" ")
c = [int(i) for i in c]

nbu = 0
nbp = 0

for i in c:
    if i == -1:
        if nbp>0:
            nbp-=1
        else:
            nbu+=1
    else:
        nbp+=i
print(nbu)