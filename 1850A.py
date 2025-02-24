n=int(input())
r = []
for _ in range(n):
    values = input().split(" ")
    values = sorted(values)
    if int(values[-1]) + int(values[-2]) >= 10 :
        r.append("YES")
    else :
        r.append("NO")

print('\n'.join(i for i in r))