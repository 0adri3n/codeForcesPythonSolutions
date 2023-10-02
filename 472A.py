n = int(input())

if (n <= 11): 
    if (n == 8): 
        print("4 4", end = " ") 
    if (n == 10): 
        print("4 6", end = " ") 
    else: 
        print("-1", end = " ") 
if (n % 2 == 0): 
    print("4 ", (n - 4), end = " ") 
else: 
    print("9 ", n - 9, end = " ") 