n=int(input())
r = []

def valid(word) :

    name = ["T", "i", "m", "u", "r"]
    for l in word :
        if l not in name :
            return False
    return True
    

for _ in range(n):

    l = int(input())
    inp = input()
    if len(inp) == 5 :
        if valid(inp) :
            r.append("YES")
        else :
            r.append("NO")
    else :
        r.append("NO")


print('\n'.join(i for i in r))