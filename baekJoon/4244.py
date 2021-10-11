import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    temp = list(map(int,sys.stdin.readline().split()))
    arr.append(temp)

for i in range(num):
    sum=0
    avg=0
    count=0
    arrLength = len(arr[i])
    for j in range(1,arrLength):
        sum+=arr[i][j]
    avg= sum/(arrLength-1)
    for k in range(1,arrLength):
        if(arr[i][k]>avg):
            count+=1
        else:
            continue
    stAvg=float(count/(arrLength-1)*100)
    print("{:.3f}%".format(stAvg))
