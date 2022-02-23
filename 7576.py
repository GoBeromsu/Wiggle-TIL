import sys
from collections import deque
m,n=map(int,sys.stdin.readline().split())
mp=[]
q= deque()
dx,dy=[-1,1,0,0],[0,0,-1,1]
res=0

for i in range(n):
    mp.append(list(map(int,sys.stdin.readline().split())))

def find(mp):
    global q
    for i in range(n):
        for j in range(m):
            if mp[i][j]== 1:
                q.append([i,j])

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<m and mp[nx][ny]==0:
                mp[nx][ny]=mp[x][y]+1
                q.append([nx,ny])

find(mp)
bfs()

for i in mp:
    for j in i:
        if j==0:
            print(-1)
            exit()
    res=max(res,max(i))
print(res-1)