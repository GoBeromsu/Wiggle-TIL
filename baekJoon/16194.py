import sys

num = int(sys.stdin.readline())
P = [0]+list(map(int,sys.stdin.readline().split()))
dp = [False for i in range(num+1)]

# 카드 1개 1
# 카드 2개 1+1 5
# 카드 3개 1+1+1 1+5 6
# 카드 4개 1+1+1+! 1+6 1+1+5 7 5+5
for i in range(1,num+1):
    for j in range(i+1):
        if dp[i]==False:
            dp[i]=dp[i-j]+P[j]
        else:
            dp[i] = min(dp[i],dp[i-j]+P[j])

print(dp[num])