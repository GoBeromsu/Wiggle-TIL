import sys

num = int(sys.stdin.readline())

def fac(num):
    if(num==0 or num ==1):
        return 1
    else:
        return fac(num-1)*num

print(fac(num))