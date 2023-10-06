m = 0
c = 0
for _ in range(int(input())):
    a, b = input().split()
    if int(a) > int(b):
        m+=1
    elif int(a) < int(b):
        c+=1
if m>c:
    print("Mishka")
elif m<c:
    print("Chris")
else:
    print("Friendship is magic!^^")