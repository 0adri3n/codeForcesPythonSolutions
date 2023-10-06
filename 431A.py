c = [int(i) for i in input().split()]
s = input()
t = 0
for i in s:
    t+=c[int(i)-1]
print(t)