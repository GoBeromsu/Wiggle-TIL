import sys
from collections import deque
b = sys.stdin.readline().rstrip()

dq = deque()

for s in b:
    if not dq:
        dq.append(s)
    elif dq[-1]!=s:
        dq.pop()
    else:
        dq.append(s)

if dq:
    print('NO')
else:
    print('YES')
