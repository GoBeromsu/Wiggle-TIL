import sys

num = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(num)]

for i in range(num):
    for j in range(i):
        if numbers[j]<numbers[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))
