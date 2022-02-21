import sys

n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
sums = [0,numbers[0]]

for num in range(2,len(numbers)+1):
    sums.append(sums[num-1]+numbers[num-1])

for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    print(sums[end]-sums[start-1])