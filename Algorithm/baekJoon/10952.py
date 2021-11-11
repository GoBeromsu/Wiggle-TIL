import sys

a=1
b=1
arr=[]

while(a!=0 and b!=0):
    a,b=map(int,sys.stdin.readline().split())
    arr.append(a+b)

for i in range(len(arr)-1):
    print(arr[i])
