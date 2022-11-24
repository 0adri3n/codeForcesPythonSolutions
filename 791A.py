limak, bob = input().split()
limak=int(limak)
bob=int(bob)
y=0
while limak<=bob:
    y+=1
    limak*=3
    bob*=2

print(y)
