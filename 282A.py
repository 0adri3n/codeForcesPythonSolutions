n=int(input())
x=0
for i in range(n):
    v=input()
    if v[2] == "+" or v[0] == "+":
        x+=1
    elif v[0] == "-" or v[2] == "-":
        x-=1
print(x)
