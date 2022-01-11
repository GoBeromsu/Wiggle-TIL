import sys

input = int(sys.stdin.readline())

# 1 2-7 19 37

n=1
sum=1
bsum=0
while True:
    sum+=(n-1)*6
    if(bsum<input and input<=sum):
        print(n)
        break
    n+=1
    bsum=sum