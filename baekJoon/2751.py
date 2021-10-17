import sys

num = int(sys.stdin.readline())
arr = []
for i in range(num):
    arr.append(int(sys.stdin.readline()))
min = arr[0]
for i in range(0,num):
    for j in range(i,num):
        if(arr[j]<=min):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        min = arr[i]
for i in range(num):
    print(arr[i])