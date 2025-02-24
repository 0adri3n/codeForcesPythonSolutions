results = []

for _ in range(int(input())) : 

    a, b = input().split(" ")
    a, b = int(a), int(b)

    if a > b :
        results.append(str(a-b))
    else:
        results.append(str(b-a))
    
for r in results :
    print(r)
