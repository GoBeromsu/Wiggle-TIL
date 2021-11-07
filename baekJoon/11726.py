import sys


num = int(sys.stdin.readline())
dp = [0,1,2] + [0]* (num-2) 
for i in range(3,num+1):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[num]%10007)