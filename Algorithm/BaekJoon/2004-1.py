import sys
# 시간 초과
n,m =map(int, sys.stdin.readline().split())

def numberCount(num,divNum):
    cnt=0
    for n in range(2,num+1):
        while n%divNum==0:
            n/=divNum
            cnt+=1
    return cnt

print(min(numberCount(n, 2),numberCount(n, 5))-min(numberCount(m,2), numberCount(m, 5))-min(numberCount(n-m,2), numberCount(n-m,5)))