k, n, w=input().split()
banana=0
sumunai=0
for i in range(int(w)+1): sumunai+=i
cost=int(k)*sumunai

if int(n)>=cost: print(0)
else: print(cost-int(n))
