_len = int(input())
c = [int(i) for i in input().split(" ")]

m = max(c)
c.remove(m)

t = 0

for i in c:
    t+=m-i
print(t)