n=int(input())
r = []
for _ in range(n):
    values = input().split(" ")
    c_values = [values.count(i) for i in values]
    r.append(values[c_values.index(1)])

print('\n'.join(i for i in r))
        