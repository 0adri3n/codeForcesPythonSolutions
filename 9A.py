from fractions import Fraction
a, b = input().split()
a, b = int(a), int(b)
if Fraction(6-(max(a, b)-1), 6) == 1:
    print("1/1")
else:
    print(Fraction(6-(max(a, b)-1), 6))