n, k = input().split()
players=input().split(" ")
minscore=players[int(k)-1]
cpmt=0
for p in players:
   if int(p)>=int(minscore) and int(p)>0:cpmt+=1
if cpmt==0:print(0)
else:print(cpmt)
