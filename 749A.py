n = int(input())

if n % 2 == 0:
    k = n // 2
    primes = [2] * k
else:
    k = (n - 3) // 2 + 1
    primes = [2] * ((n - 3) // 2) + [3]

print(k)
print(" ".join(map(str, primes)))

