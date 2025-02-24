results = []

for _ in range(int(input())) : 

    s1, s2, s3, s4 = input().split(" ")
    s1, s2, s3, s4 = int(s1), int(s2), int(s3), int(s4)

    w1 = s1 if s1 > s2 else s2
    l1 = s2 if s1 > s2 else s1
    w2 = s3 if s3 > s4 else s4
    l2 = s4 if s3 > s4 else s3

    # print(f"w1 : {w1} & l1 : {l1} | w2 : {w2} & l2 : {l2}")

    if w1 > l2 and w2 > l1 :
        results.append("YES")
    else :
        results.append("NO")

for r in results :
    print(r)

    