n=int(input())
s=input().split()
for i in range(n):
    print(s.index(str(i+1))+1, end=" ")
