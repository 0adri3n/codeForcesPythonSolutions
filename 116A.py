n=int(input())
trampop=0
max=0
for i in range(n):
    s, e=input().split()
    s, e=int(s), int(e)
    trampop-=s
    trampop+=e
    if trampop>max: max=trampop
print(max)
