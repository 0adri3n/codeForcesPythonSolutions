r = []

for _ in range(int(input())) :

    coins = [int(i) for i in input().split(" ")]

    n = coins[-1]/3
    s = 0
    for c in range(len(coins)-1) :

        coins[c] += n

    ck = len(set(coins[:-1]))
    print(ck)
    print("set", coins[:-1])
    print("coins moyenne", sum(coins[:-1]) / len(coins[:-1]))
    if ck == 1 :
        r.append("YES")
    else :
        r.append("NO")

print("\n".join(r))