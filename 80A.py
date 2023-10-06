def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

a, b = input().split()
a, b = int(a), int(b)

p = a+1
f = False
while not f:
    if is_prime(p):
        f = True
    else:
        p+=1
        
if p==b:
    print("YES")
else:
    print("NO")