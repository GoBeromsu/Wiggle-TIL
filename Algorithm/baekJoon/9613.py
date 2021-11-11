import sys

def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y, x%y)

num = int(sys.stdin.readline())

for _ in range(num):
    sum = 0
    number = list(map(int,sys.stdin.readline().split()))
    for x in range(1,number[0]):
        for y in range(x+1,number[0]+1):
            val = gcd(number[x],number[y])
            sum+=val
    print(sum)
