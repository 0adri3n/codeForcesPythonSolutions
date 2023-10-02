_len = int(input())
c = [int(i) for i in input().split(" ")]

s = 0
d = 0

i = 1
while len(c) > 0:
    if i%2 != 0:
        if c[0] > c[-1]:
            s += c[0]
            c.remove(c[0])
        else:
            s += c[-1]
            c.remove(c[-1])
    else:
        if c[0] > c[-1]:
            d += c[0]
            c.remove(c[0])
        else:
            d += c[-1]
            c.remove(c[-1])

    i+=1

print(str(s) + " " + str(d))