import sys

n,k = map(int,sys.stdin.readline().split())
coins=[int(sys.stdin.readline()) for i in range(n)]
cnt=0


for i in range(n-1,-1,-1):
    if k==0:
        break
    if coins[i]>k:
        continue
    cnt+=k//coins[i]
    k%=coins[i]
print(cnt)