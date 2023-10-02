n = int(input())
nni = input()
nni = nni.split(" ")
nni = [int(i) for i in nni]

def mini(list):
    return min(list)
    
def maxi(list):
    return max(list)

rec = []
rec.append(nni[0])
a = 0

for i in range(1, n):
    tL = nni[0:i+1]

    if nni[i] <= mini(tL) or nni[i] >= maxi(tL):
        if nni[i] not in rec:
            a+=1
            rec.append(nni[i])
 
print(a)