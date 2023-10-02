n, k = input().split()
n, k = int(n), int(k)

m = [int(i) for i in input().split()]
am = []
for i in m:
    if i+k<=5:
        am.append(i)
print(len(am)//3)