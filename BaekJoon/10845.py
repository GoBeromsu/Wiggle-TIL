import sys

num = int(sys.stdin.readline())
que = []
for i in range(num):
    word = sys.stdin.readline().rstrip().split()
    order = word[0]
    if order == 'push':
        que.append(int(word[1]))
    elif order == 'pop':
        if not que:
            print(-1)
        else:
            num = que[0]
            que.remove(num)
            print(num)
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif order == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
   