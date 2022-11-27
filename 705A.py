n=int(input())
res=""
if n>1:
    for i in range(n-1):
        if i%2!=0:
            res+="I love that "
        else: res+="I hate that "
if n%2==0:
    res+="I love it"
else: res+="I hate it"
print(res)
