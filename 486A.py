n=int(input())
s=0
for i in range(n+1):
    if i%2==0:
        s+=i
    else:
        s-=i
        
print(s)
