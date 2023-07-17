import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
MAX=100000
clock = [0 for i in range(MAX+1)]


def bfs(n):
    q= deque([n])
    while q:
        x=q.popleft()
        if x==k:
            return clock[x]
        for i in (x-1,x+1,x*2):
            if 0<=i <=MAX and not clock[i]:
                clock[i]=clock[x]+1
                q.append(i)
print(bfs(n))