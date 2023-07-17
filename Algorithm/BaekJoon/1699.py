import sys
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 2 3 1 2 3 4 2 1 02 03 04 02 03 04

num = int(sys.stdin.readline())
dp = [i for i in range(num+1)]

for i in range(2,num+1):
    pow = int(i**0.5)
    for j in range(1,pow+1):
        dp[i]=min(dp[i],dp[i-j*j]+1)

print(dp[num])