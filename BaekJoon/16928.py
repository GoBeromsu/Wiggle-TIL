import sys
from collections import deque

N,M= map(int, sys.stdin.readline().split())

mp=[0 for _ in range(101)]
check = [0 for _ in range(101)]
ans=[]
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    mp[x]=y
    check[x]=True
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    mp[x]=y
    check[x]=False

# 참 : 사다리, 거짓 : 뱀

def bfs(x):
    pass