import sys
from collections import deque

dq= deque()
arr = []
N,K = map(int,sys.stdin.readline().split())

for n in range(N):
    dq.append(n+1)

while dq:
    for k in range(K-1):
        temp = dq.popleft()
        dq.append(temp)
    val = dq.popleft()
    
    arr.append(val)

print("<",end='')
for i, num in enumerate(arr):
    if i==len(arr)-1:
        print(f'{num}>')
    else:
        print(f"{num},",end=' ')
