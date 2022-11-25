n=int(input())
s=input()
s=s.split(" ")
h=False
for l in s:
    if l=="1": h=True

if h:print("HARD")
else:print("EASY")
