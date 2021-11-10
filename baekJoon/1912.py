import sys

num = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp=[-1001]*num
for i in range(num):
    dp[i]=max(numbers[i],dp[i-1]+numbers[i])
print(max(dp))