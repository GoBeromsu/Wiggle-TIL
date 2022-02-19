import sys

t = int(sys.stdin.readline())
dp = [1]*3 + [0]*97

for i in range(3,100):
    dp[i]=dp[i-2]+dp[i-3]

for i in range(t):
    num=int(sys.stdin.readline())
    print(dp[num-1])