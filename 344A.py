n=int(input())
magnets=[]
for i in range(n):
    magnet=input()
    magnets.append(magnet)

group=1
for i in range(len(magnets)-1):
    if magnets[i]!=magnets[i+1]:
        group+=1

print(group)
