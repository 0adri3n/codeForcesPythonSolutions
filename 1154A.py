x1, x2, x3, x4 = [int(i) for i in input().split(" ")]

m = max(x1, x2, x3, x4)

if m == x1:
    a = m - x2
    b = m - x3
    c = m - x4

    print(str(a) + " " + str(b) + " " +str(c) + " ")

elif m == x2:

    a = m - x1
    b = m - x3
    c = m - x4

    print(str(a) + " " + str(b) + " " +str(c) + " ")

elif m == x3:

    a = m - x1
    b = m - x2
    c = m - x4

    print(str(a) + " " + str(b) + " " +str(c) + " ")

elif m == x4:

    a = m - x1
    b = m - x2
    c = m - x3

    print(str(a) + " " + str(b) + " " +str(c) + " ")