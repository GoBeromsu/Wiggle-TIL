import sys
from collections import deque

deq = deque()

num = int(sys.stdin.readline())

for n in range(num):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push_front':
        deq.appendleft(int(word[1]))
    elif order == 'push_back':
        deq.append(word[1])
    elif order == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif order == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())    
    elif order == 'size':
        print(len(deq))
    elif order == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif order == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])