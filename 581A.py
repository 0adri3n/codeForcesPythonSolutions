a, b = [int(i) for i in input().split(" ")]

mini = min(a, b)
maxi = max(a, b)
maxi -= mini

print(str(mini) + " " + str(maxi//2))