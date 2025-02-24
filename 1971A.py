r = []

for _ in range(int(input())) :

    x, y = input().split(" ")
    x, y = int(x), int(y)

    mini = min([x, y])
    maxi = max([x, y])

    r.append(f'{mini} {maxi}')

print("\n".join(r))