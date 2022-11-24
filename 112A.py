fs=input()
ss=input()
def cmp(a, b):
    return (a>b) - (a<b)
print(str(cmp(fs.lower(), ss.lower())))
