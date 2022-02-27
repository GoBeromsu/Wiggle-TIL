import sys
from collections import deque

n = int(sys.stdin.readline())
mp=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

nodes=[[] for i in range(n)]

for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j]==1:
            nodes[i].append(j)

def bfs(node):
    q=deque()
    visited=[False]*n
    for i in nodes[node]:
        q.append(i)
        visited[i]=True

    while q:
        x=q.popleft()
        for i in nodes[x]:
            if not visited[i]:
                visited[i]=True
                mp[node][x]=1
                q.append(i)
                nodes[node].append(i)
                mp[node][i]=1
for i in range(n):
    bfs(i)

for m in mp:
    print(*m)
