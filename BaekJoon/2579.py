import sys

# 계단은 한 계단씩 또는 두 계단씩 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안된다.
# 마지막 도착 계단은 반드시 밟아야한다.

n = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for i in range(n)]
# dp[i] = max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-1])
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])

for i in range(3,n):
    dp[i] = max(stair[i]+dp[i-2],stair[i-1]+stair[i]+dp[i-3])
print(dp[n-1])