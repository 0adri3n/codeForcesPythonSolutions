n = input()
n = [int(i) for i in n.split(" ")]
n = sorted(n)
a, b, c = int(n[0]), int(n[1]), int(n[2])

mini = 0
minis = abs((a-a))+abs((b-a))+abs((c-a))

for i in range(a+1, c+1):
    s=abs((a-i))+abs((b-i))+abs((c-i))
    if s<minis:
        minis=abs((a-i))+abs((b-i))+abs((c-i))
        mini=i
    
print(minis)


    
        