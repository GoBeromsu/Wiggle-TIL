import sys

arr= []

num = int(sys.stdin.readline())

for i in range(num):
    arr.append(sys.stdin.readline())

for i in range(num):
    sum =0
    count=0
    for j in range(len(arr[i])):
        if(arr[i][j]=='O'):
            count+=1
            sum+=count
        else:
            count=0
        if(j==(len(arr[i])-1)):
            print(sum)
            
