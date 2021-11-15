import sys

num = int(sys.stdin.readline())
numbers = [0]*10003
for i in range(1,num+1):
    numbers[i]=int(sys.stdin.readline())
dp = [0]*10003
dp[1]=numbers[1]
dp[2]=numbers[1]+numbers[2]

for i in range(3,num+1):
    dp[i]=max(dp[i - 1], dp[i - 3] + numbers[i - 1] + numbers[i], dp[i - 2] + numbers[i])
print(dp[num])
