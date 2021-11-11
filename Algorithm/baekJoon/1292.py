import sys

n,k = map(int,sys.stdin.readline().split())
arr = []

for i in range(1,1001):
    for j in range(i):
        arr.append(i)

print(sum(arr[n-1:k]))