n, k, l, c, d, p, nl, np = [int(i) for i in input().split(" ")]
ml = (k*l)/nl
limes = c*d
salt = p/np
print(int(min(ml, limes, salt)//n))