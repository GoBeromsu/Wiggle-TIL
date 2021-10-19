import sys

nm= list(map(int,sys.stdin.readline().split()))

n= nm[0]
m = nm[1]
arr=[]

val = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    arr.append(val[i])

arr = sorted(arr)
arrLength = len(arr)
max = 0
for i in range(arrLength):
    for j in range(i+1,arrLength):
        for k in range(j+1,arrLength):
            number=arr[i]+arr[j]+arr[k]
            if(number<= m and max<number):
                max = number
print(max)