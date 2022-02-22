import sys
from collections import deque

sys.setrecursionlimit(10000)
# 방향 없는 그래프가 주어졌을 때, 연결 요소 개수 세는 법

n, m = map(int, sys.stdin.readline().split())
nodes = [[] for i in range(n + 1)]
check = [False for _ in range(n + 1)]

cnt = 0
for i in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)
    nodes[node1].sort()
    nodes[node2].sort()

def bfs(node):
    check[node] == True
    q = deque([node])
    while q:
        v = q.popleft()
        for i in nodes[v]:
            if not check[i]:
                check[i] = True
                q.append(i)

for i in range(1, n + 1):
    if not check[i]:
        cnt += 1
        bfs(i)

print(cnt)
