n=int(input())
rooms=0
for i in range(n):
    room=input().split(" ")
    if int(room[0])<int(room[1])-1:rooms+=1
print(rooms)
