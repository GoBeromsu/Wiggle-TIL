import sys

def f(x):
    if (x==1 or x==2):
        return 1
    return f(x-2)+f(x-1)

for i in range(1,1000,1):
    print(f(i))

