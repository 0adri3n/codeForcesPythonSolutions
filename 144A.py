n = input()
line = list(map(int, input().split(" ")))
minimum = min(line)
maximum = max(line)
count = line.index(maximum)
line.pop(count)
line.insert(0, count)
line.reverse()
count += line.index(minimum)
print(count)