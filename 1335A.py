import math
t = int(input())

s=""

for i in range(t):

    n = int(input())
    
    if n<2*10**9:
    
        if n>1:
            
            if n%2 == 0:
                s+=str(int((n/2)-1)) + "\n"
            
            else:
                s+=str(int(math.floor(n/2))) + "\n"
        
        else:
            s+=str("0") + "\n"
    
    else:
        s+=str("999999999") + "\n"

print(s)