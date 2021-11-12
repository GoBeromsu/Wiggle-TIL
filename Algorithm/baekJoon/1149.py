import sys

n = int(sys.stdin.readline())
dp = [[0]*3 for i in range(n)]
numbers=[]
for i in range(n):
    numbers.append(list(map(int,sys.stdin.readline().split())))
dp[0]=numbers[0]
for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+numbers[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+numbers[i][1]
    dp[i][2]=min(dp[i-1][1],dp[i-1][0])+numbers[i][2]

print(min(dp[n-1]))