import sys

num = int(sys.stdin.readline())

for i in range(2,num+1):
    while num%i==0:
        num/=i
        print(i)