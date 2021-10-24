import sys
from collections import deque

num = int(sys.stdin.readline())

dq = deque()
for i in range(num,0,-1):
    dq.append(i)

while(len(dq)>1):
    dq.pop()
    temp = dq.pop()
    dq.appendleft(temp)

print(dq[0])