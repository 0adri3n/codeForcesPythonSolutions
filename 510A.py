entry = input()
n, m = entry.split(" ")
n, m = int(n), int(m)
left = True
for i in range(n):
    if i%2 != 0:
        if left:
            print("."*(m-1) + "#")
            left = False
        else:
            print("#" + "."*(m-1))
            left = True
    else:
        print("#"*m)
