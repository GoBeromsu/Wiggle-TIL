    import sys

    # 1 1
    # 2 1 + 1 * 2 = 3 
    # 3 1 + 2 * 2 = 5
    # 4 1 + 3 * 2 + 2 * 2 = 11
    # 5 1 + 4 * 2 + 3 * 4 = 21 

    num = int(sys.stdin.readline())

    dp = [0,1,3] + [0] * (num-2)

    for i in range(3,num+1):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(dp[num]%10007)