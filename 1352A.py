t = int(input())
number = []

for i in range(t):
    number.append(input())



for n in number:
    
    tposs = 0
    lposs = []
    
    n = list(n)
    
    for j in range(len(n)):
    
        if n[j] != "0":
            tposs+=1
            nb = str(n[j])
            nb += ((len(n)-1)-j)*"0"
            lposs.append(nb)
            
    print(str(tposs)+"\n")
    print(*lposs, sep=" " + "\n")

