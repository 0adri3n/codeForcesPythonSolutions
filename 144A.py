n=int(input())
s=list(map(int, input().split()))

sorteds=s
sorteds.sort(reverse=True)

dist=0
dist+=len(s)-1-s.index(sorteds[len(s)-1])
dist+=len(s)-1-s.index(sorteds[0])
print(dist)
