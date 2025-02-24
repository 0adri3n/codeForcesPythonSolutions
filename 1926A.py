res = []

for _ in range(int(input())) :

    array = input()
    c_a = array.count("A")
    c_b = array.count("B")
    if c_a > c_b :
        res.append("A")
    
    else :
        res.append("B")

    
for r in res :
    print(r)