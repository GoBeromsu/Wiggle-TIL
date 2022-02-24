import sys
from collections import deque

# 세 갈래로 나눈 후 또 세 갈래로 나눈 후 또 세갈래로 나누는 걸 반복해서 값이 같은 경우
def dfs(n,k):
    q=deque([n])
    while q:
        x=q.popleft()
        if x==k:
            print(dist[x])
            break
        for j in (x-1,x+1,x*2):
            if 0<=j<=10000 and not dist[j]:
                dist[j]=dist[x]+1
                q.append(j)

n,k = map(int,sys.stdin.readline().split())
dist=[0]*100000
dfs(n, k)