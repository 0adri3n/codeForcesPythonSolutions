# MY CODE DON'T WORK ON TEST #27
n=int(input())
xlvl=input().split()
ylvl=input().split()
x=set(xlvl)
y=set(ylvl)
k=x.union(y)

canPass=True
for i in range(1, n+1):
    if str(i) not in k:
        canPass=False
        break

if canPass: print("I become the guy.")
else: print("Oh, my keyboard!")

# SO HERE IS A CODE THAT I FOUND WHICH WORKS
# n = int(input());
#
# a = list(map(int, input().split()))[1:];
#
# b = list(map(int, input().split()))[1:];
#
# s = set(a);
#
# t = set(b);
#
# k = s.union(t);
#
# ok = 0;
# for i in range(1, n+1):
#     if i in k:
#         ok = 1
#     else:
#         ok = 0
#         break
# if(ok):
#     print('I become the guy.')
# else:
#     print('Oh, my keyboard!')
