import sys

num = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

dp = [x for x in numbers]
for n in range(num):
    for j in range(n):
        if numbers[n]>numbers[j]:
            dp[n]=max(dp[j]+numbers[n],dp[n])
print(max(dp))