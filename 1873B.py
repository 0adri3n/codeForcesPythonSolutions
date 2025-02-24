res = []

def add_one(digits) :

    min_d = min(digits)
    changed = False
    for i in range(len(digits)) :

        if digits[i] == min_d:

            digits[i] +=1
            return digits

for _ in range(int(input())) : 

    n = int(input())
    digits = [int(i) for i in input().split(" ")]

    digits = add_one(digits)

    p_d = 1
    for d in digits :
        p_d *= d 
    
    res.append(p_d)

for r in res :
    print(r)