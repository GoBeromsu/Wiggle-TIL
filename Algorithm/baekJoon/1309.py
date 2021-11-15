import sys

N = int(sys.stdin.readline())

dp = [[1]*3 for i in range(N)]

for i in range(1,N):
    dp[i][0]=sum(dp[i-1])%9901
    dp[i][1]=dp[i-1][0]%9901+dp[i-1][1]%9901
    dp[i][2]=dp[i-1][0]%9901+dp[i-1][1]%9901
print(sum(dp[N-1])%9901)