word=input()
capitaleCount=0
minus=0
for l in word:
    if 65<=ord(l)<=90:
        capitaleCount+=1
    else: minus+=1
if capitaleCount>minus:
    print(word.upper())
else:
    print(word.lower())
