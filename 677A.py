n, h=input().split()
n, h=int(n), int(h)
friends=input().split(" ")
road=0
for f in friends:
    if int(f)<=h:
        road+=1
    else:
        road+=2
print(road)
