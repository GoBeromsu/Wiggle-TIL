import sys

num = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(num)]
# num = 8
# numbers = [4,3,6,8,7,5,2,1]
stack = []
answer = []
cnt=0
for x,y in enumerate(numbers):
    if x==0:
        for i in range(1,y+1):
            stack.append(i)
            answer.append('+')
        cnt=y+1
        stack.pop()
        answer.append('-')
    else:
        if len(stack)==0 or y>stack[-1]:
            for i in range(cnt,y+1):
                stack.append(i)
                answer.append('+')
            stack.pop()
            answer.append('-')
            cnt=y+1
        elif y==stack[-1]:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            answer.append(1)
            break

if 1 not in answer:
    for a in answer:
        print(a)