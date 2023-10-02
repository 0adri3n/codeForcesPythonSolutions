lb = list(input())
res = []

i=0
while i<len(lb):
    if lb[i] == ".":
        res.append("0")
        i+=1
    elif lb[i] == "-" and lb[i+1] == ".":
        res.append("1")
        i+=2
    elif lb[i] == "-" and lb[i+1] == "-":
        res.append("2")
        i+=2


print(*res, sep="")