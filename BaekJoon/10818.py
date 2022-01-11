import sys

N = int(sys.stdin.readline())
num=[]
num = list(map(int,sys.stdin.readline().split()))
min=num[0]
max=num[0]

for i in range(N):
    if(num[i]<min):
        min=num[i]
    if(num[i]>max):
        max=num[i]

print("{} {}".format(min,max))