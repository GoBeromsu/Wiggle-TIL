import sys

num =int(sys.stdin.readline())

dp = [ [0]*2 for i in range(num+1)]
dp[1] = [0,1]

for n in range(2,num+1):
    dp[n][0] = dp[n-1][0] + dp[n-1][1]
    dp[n][1] = dp[n-1][0]
print(sum(dp[num]))