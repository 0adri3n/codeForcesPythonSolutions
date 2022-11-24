n=int(input())
lw=[]
for i in range(n):
   word=input()
   if len(word)>10:
      w=""
      w+=word[0]+str(len(word)-2)+word[-1]
      lw.append(w)
   else:
      lw.append(word)
for w in lw:
   print(w)

