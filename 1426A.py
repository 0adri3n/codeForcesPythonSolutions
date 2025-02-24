r = []
for _ in range(int(input())) :

    apart, x = input().split(" ")
    apart, x = int(apart), int(x)


    floor_c = 1
    if apart < 3:
        r.append("1")

    else :

        for floor in range(2, apart, x):

            floor_c +=1

        r.append(str(floor_c))

print("\n".join(r))