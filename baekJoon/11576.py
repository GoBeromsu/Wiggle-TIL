import sys

A,B = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
sum = 0
result=[]
for i in range(m):
    sum+=numbers.pop()*(A**i)

while sum:
    r = sum%B
    q = (sum-r)//B
    result.append(r)
    sum = q

while result:
    print(result.pop(),end=' ')
