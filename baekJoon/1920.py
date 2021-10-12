import sys

num = int(sys.stdin.readline())
arr=[]
for i in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    arr.append(temp)

for i in range(num):
    for j in range(len(arr[i])):
        if (arr[i][j]==num):
            print(1)
            break
        if((j+1)==len(arr[i])):
            print(0)