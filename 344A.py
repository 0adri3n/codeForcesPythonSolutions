grp = 0
av = ""

for _ in range(int(input())):
    mtn = input()
    if mtn != av:
        grp+=1
        av=mtn
print(grp)    

# WRITED IN JAVA CUZ OF TIME LIMIT EXCEDEED ON TEST 7