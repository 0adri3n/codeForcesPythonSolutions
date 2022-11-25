nb=input()
lucky=True
luckycount=0
i=0
luckylist=["4", "7"]
while i<len(nb):
    if nb[i] in luckylist: luckycount+=1
    i+=1

if str(luckycount) in luckylist: print("YES")

else: print("NO")
