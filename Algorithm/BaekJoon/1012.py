import sys
from collections import deque
t = int(sys.stdin.readline())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(mp,a,b):
    queue = deque()
    queue.append((a,b))
    mp[a][b]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny <0 or ny>= m:
                continue
            if mp[nx][ny]==1:
                mp[nx][ny]=0
                queue.append((nx,ny))

for i in range(t):
    count=0
    n,m,k = map(int,sys.stdin.readline().split())
    mp = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int,sys.stdin.readline().split())
        mp[x][y]=1
    for a in range(n):
        for b in range(m):
            if mp[a][b]==1:
                bfs(mp, a, b)
                count+=1
    print(count)