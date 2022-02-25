import sys
from collections import deque
n,m= map(int, sys.stdin.readline().split())

persons = [[] for _ in range(n+1)]
kebin = [0 for _ in range(n+1)]
for i in range(1,m+1):
    p1,p2 = map(int,sys.stdin.readline().split())
    persons[p1].append(p2)
    persons[p2].append(p1)
    persons[p1].sort()
    persons[p2].sort()

def bfs(person):
    q = deque([person])
    check,count=[],[0]*(n+1)
    while q:
        x=q.popleft()
        for i in persons[x]:
            if i not in check:
                count[i]=count[x]+1
                check.append(i)
                q.append(i)
    kebin[person]=sum(count)
for i in range(1,n+1):
    bfs(i)


print(kebin.index(min(kebin[1:])))