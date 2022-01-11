import sys

stack = []
orders = []

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
def empty():
    if not stack:
        return 1
    else:
        return 0
def top():
    if not stack:
        return -1
    else:
        return stack[-1]
def push(num):
    stack.append(num)
def size():
    return len(stack)

def switch(key):
    dic ={'top':top(),'size':size(),'empty':empty()}
    return dic[key]
num = int(sys.stdin.readline())



for n in range(num):
    order = sys.stdin.readline().rstrip().split() 
    length = len(order)
    if length == 1:
        orders.append(order)
    else:
        orders.append(order)
for order in orders:
    if order[0] == 'pop':
        print(pop())
    elif len(order) ==1:
        print (switch(order[0]))
    else:
        stack.append(order[1])
    # print(f"현재 명령어는 {order}stack is {stack}")
