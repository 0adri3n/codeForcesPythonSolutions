res = []
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
from math import floor
for _ in range(int(input())):

    _len = int(input())

    n = [int(i) for i in input().split()]

    print(list(chunks(n, floor(_len/2))))

# DONT WORK