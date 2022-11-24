x=int(input())
step=0
eleP=0
while eleP<x:
    if x-eleP>=5:eleP+=5
    elif x-eleP>=4:eleP+=4
    elif x-eleP>=3:eleP+=3
    elif x-eleP>=2:eleP+=2
    elif x-eleP>=1:eleP+=1
    step+=1
print(step)
