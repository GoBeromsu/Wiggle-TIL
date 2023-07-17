import sys

n = int(sys.stdin.readline())
dp = [0,1]

for i in range(2,N+1):
    # min_value는 최댓값을 미리 설정해둠
    min_value = sys.maxsize
    # j는 제곱근
    j=1
    while (j**2)<=i:
# 자기보다 작은 제곱 수들을 뺀 값들 중
#  자릿 수가 가장 작은 값을 구하면 되는게 아닌가?
        min_value = min(min_value,dp[i-(j**2)])
        j+=1
    dp.append(min_value+1)
print(dp[n])