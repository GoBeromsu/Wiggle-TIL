import sys
from collections import deque


N,M = map(int,sys.stdin.readline().split())
mp = []
for i in range(M):
    mp.append(list(sys.stdin.readline().rstrip()))

visited=[[False] * N for _ in range(M)]
W, B = [], []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    color = mp[x][y]
    count=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue    
            if color==mp[nx][ny] and visited[nx][ny]==False:
                visited[nx][ny]=True
                q.append((nx,ny))
                count+=1
    if count==0:
        count=1
    if color=='W':
        W.append(count)
    else:
        B.append(count)
    
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

answer=[]
for i in (W,B):
    ans=0
    for j in i:
        ans+=j**2
    answer.append(ans)
print(*answer)