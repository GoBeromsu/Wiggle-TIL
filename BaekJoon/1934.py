import sys

def euclid(x,y):
    if x%y==0:
        return y
    else:
        return euclid(y, x%y)

for i in range(int(sys.stdin.readline())):
    x,y = map(int,sys.stdin.readline().split())
    m = euclid(x, y)
    print(int(x*y/m))