import sys

num = int(sys.stdin.readline())
numbers=[list(map(int,sys.stdin.readline().split())) for i in range(num)]
dp = [[0 for n in range(len(numbers[i])) ]for i in range(num)]

dp[0]=numbers[0]

for n in range(1,num):
    for j in range(n+1):
        if j ==0:
            dp[n][j] = dp[n-1][0] + numbers[n][j]
        elif j == n:
            dp[n][j] = dp[n-1][n-1]+numbers[n][j]
        else:
            dp[n][j] = max(dp[n-1][j-1],dp[n-1][j]) + numbers[n][j]
print(max(dp[num-1]))