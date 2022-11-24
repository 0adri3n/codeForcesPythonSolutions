mat=[]
for i in range(5):
    x=input()
    mat.append(x.split(" "))

for i in range(5):
    for j in range(5):
        if mat[i][j]=="1":
            x,y=i,j
moves=0
while x != 2:
    if x>2:
        x-=1
        moves+=1
    elif x<2:
        x+=1
        moves+=1
while y != 2:
    if y>2:
        y-=1
        moves+=1
    elif y<2:
        y+=1
        moves+=1

print(moves)
