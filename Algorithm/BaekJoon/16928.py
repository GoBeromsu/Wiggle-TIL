import sys


from collections import deque

N, M = map(int, sys.stdin.readline().split())
sl= [0 for _ in range(101)]
visited=[False]*101
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    sl[x]=y

for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    sl[x]=y

q=deque()
q.append((1,0))
visited[1]=True

ans=999999

while q:
    front=q.popleft()
    if front[0]==100:
        ans=min(ans,front[1])
        continue
    for i in range(1,7):
        new = front[0]+i
        if new>100:continue
        if visited[new]==True:
            continue
        visited[new]=True
        if sl[new]!=0:
            new = sl[new]
        q.append((new,front[1]+1))
print(ans)