import sys

n = int(sys.stdin.readline())
arr =[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0 for i in range(max(arr)+1)]
dp[1],dp[2],dp[3] = 1,2,4

for i in range(4,len(dp)):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for a in arr:
    print(dp[a])