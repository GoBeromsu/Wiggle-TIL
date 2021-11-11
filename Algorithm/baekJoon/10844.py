import sys

# 1 : 1 2 3 4 5 6 7 8 9
# 2 : 10 12. 21 23. 32 34. 43 45. 54 56. 65 67. 76 78. 87 89. 98 90?
# 3 : 101 .121 123.  

num = int(sys.stdin.readline())

dp = [[0 for i in range(10)] for i in range(num+1)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]

MOD = 1000000000

for i in range(2,num+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif j==9:
            dp[i][j]= dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[num])%MOD)