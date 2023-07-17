import sys

stack1=list(sys.stdin.readline().rstrip())
stack2=[]
num = int(sys.stdin.readline())


for i in range(num):
    temp = sys.stdin.readline().rstrip()
    if ' ' not in temp:
        order = temp
    else:
        order,val = map(str,temp.split())
    if order == 'P':
        stack1.append(val)
    elif order == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif order == 'D' :
        if stack2:
            stack1.append(stack2.pop())
    elif order == 'B':
        if stack1:
            stack1.pop()

print(''.join(stack1)+''.join(stack2[::-1]))