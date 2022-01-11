import sys

# 1 1 
# 2 1 + 1 = 2
# 3 1 + 2 = 4
# 4 1 + 3 + 1 + 2 = 7
# 5 1 + 4 + 3 + 2 + 3 = 13
num = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(num)]
dp = [ 0 , 1 ,2 ,4] + [0] * max(numbers)

def getDp(n):
    if dp[n]!=0:
        return dp[n]
    else:
        dp[n] = getDp(n-2)+ getDp(n-1) + getDp(n-3)
        return dp[n]


for n in numbers:
    print(getDp(n))
