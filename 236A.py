nickname=input()
letters=[]
for l in nickname:
    if l not in letters:
        letters.append(l)
if len(letters)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
