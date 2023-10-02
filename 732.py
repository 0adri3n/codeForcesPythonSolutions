k, r = [int(i) for i in input().split(" ")]

n = 0
ans = int()

while True:
    if n != 0 and (10*n) % k == 0:
        ans = (10 * n) // k
        break
    if (10 * n + r) % k == 0:
        ans = (10 * n + r) // k
        break
    n += 1
print(ans)