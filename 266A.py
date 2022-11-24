n=int(input())
s=input()
s=list(s)

index=0
index2=1
moves=0
while index2<len(s):
    if s[index]==s[index2]: moves+=1
    index+=1
    index2+=1
print(moves)
