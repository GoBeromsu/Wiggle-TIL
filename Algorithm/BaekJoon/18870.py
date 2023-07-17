import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
sNumbers = sorted(list(set(numbers)))
numDic={}
for num in numbers:
    numDic[num]=0

for i in range(len(sNumbers)):
    numDic[sNumbers[i]]=i

for i in range(n):
    print(numDic[numbers[i]], end=' ' )


    