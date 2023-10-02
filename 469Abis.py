n = int(input());

a = list(map(int, input().split()))[1:];

b = list(map(int, input().split()))[1:];

s = set(a);

t = set(b);

k = s.union(t);

ok = 0;
for i in range(1, n+1):
    if i in k:
        ok = 1
    else:
        ok = 0
        break
if(ok):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
