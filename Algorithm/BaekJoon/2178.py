import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
mp=[]

for _ in range(N):
    mp.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited = [[0]*M for _ in range(N)]

q=deque([(0,0)])
while q:
    x,y =q.popleft()
    if x==N-1 and y==M-1:
        print(visited[x][y]+1)
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]

        if 0<= nx <N and 0<= ny<M:
            if visited[nx][ny] ==0 and mp[nx][ny]==1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))