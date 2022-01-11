import sys

num = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
# num = 10
# numbers = [1,5,2,1,4,3,4,5,2,1]
rNumbers =numbers[::-1]
dpl,dpr = [0]*num,[0]*num

for i in range(num):
    for j in range(i):
        if numbers[i]>numbers[j]:
            dpl[i]=max(dpl[i],dpl[j]+1)

for i in range(num):
    for j in range(i):
        if rNumbers[i]>rNumbers[j]:
            dpr[i]=max(dpr[i],dpr[j]+1)
result =[x+y for x,y in zip(dpl,dpr[::-1])]

print(max(result)+1)