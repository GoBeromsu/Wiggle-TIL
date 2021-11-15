import sys

# 1 : 0 1 2 3 4 5 6 7 8 9
# 2 : 00-09 11-19 22-29 33-39 44-49 55-59 66-69 77-79 88-89 99
# 3 : 000-099 11-99
n = int(sys.stdin.readline())

dp = [[1]*10 for i in range(n)]

for i in range(1,n):
    for j in range(8,-1,-1):
        dp[i][j]=dp[i-1][j]%10007+dp[i][j+1]%10007
print(sum(dp[n-1])%10007)