n=int(input())
nbprob=0
for i in range(n):
   prob=input()
   prob=prob.split(" ")
   sure=0
   for l in prob:
      if int(l) == 1:sure+=1
   if sure > 1:nbprob+=1
print(nbprob)
