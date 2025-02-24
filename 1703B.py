results = []

for _ in range(int(input())) : 

    l = int(input())
    probs = input()

    t_b = 0
    l_b = []

    for b in probs : 

        if b not in l_b :

            t_b += 2
            l_b.append(b)
        
        else :

            t_b +=1

    results.append(t_b)

for result in results :
    print(result)