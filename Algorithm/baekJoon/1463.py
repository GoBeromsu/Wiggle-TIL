import sys

num = int(sys.stdin.readline())

dp = [0 for i in range(num+1)]

for i in range(2,num+1):
    dp[i] +=1
    if i%3 ==0:
        dp[i]= dp[i//3] +1
    if i%2 == 0:
        dp[i]=dp[i//2]+1

print(dp[num])