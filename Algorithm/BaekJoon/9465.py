import sys


def solve():
    l = int(sys.stdin.readline())
    dp = [[0]*l for i in range(3)]
    arr =[]
    for i in range(2):
        arr.append(list(map(int,sys.stdin.readline().split())))

    for i in range(l):
        if i==0:
            dp[1][i]=arr[0][i]
            dp[2][i]=arr[1][i]
        else:
            dp[0][i]=max(dp[1][i-1],dp[2][i-1])
            dp[1][i]=max(dp[0][i-1],dp[2][i-1])+arr[0][i]
            dp[2][i]=max(dp[0][i-1],dp[1][i-1])+arr[1][i]
    print(max(max(dp[0][l-1],dp[1][l-1]),dp[2][l-1]))

n = int(sys.stdin.readline())
for i in range(n):
    solve()