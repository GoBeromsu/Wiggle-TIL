import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    op = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline())
    ar = list(sys.stdin.readline().rstrip()[1:-1].split(","))
    ar = deque(ar)
    
    toggle=False
    oob=False

    if num==0:
        ar=deque([])

    for o in op:
        if o == "R":
            toggle = not toggle
        else:
            if len(ar)==0:
                oob=True
                break
            if toggle:
                ar.pop()
            else:
                ar.popleft()
    if oob:
        print('error')       
    else:
        if toggle:
            ar.reverse()
        print("[" + ",".join(ar) + "]")