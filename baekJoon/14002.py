import sys

num = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

dp = [1 for i in range(num)]

for i in range(num):
    for j in range(i):
        if numbers[i]>numbers[j]:
            dp[i] = max(dp[i],dp[j]+1)
        
maxLen = max(dp)
print(maxLen)
idx = dp.index(maxLen)
result = []

while idx>=0:
    if dp[idx]==maxLen:
        result.append(numbers[idx])
        maxLen-=1
    idx-=1
while result:
    print(result.pop(),end=' ')