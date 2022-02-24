import sys
from collections import deque

sen =sys.stdin.readline().rstrip()
sentence = deque([i for i in sen])
numbers,op=[],[]

temp=''
while sentence:
    x = sentence.popleft()
    if 48<=ord(x)<=57:
        temp+=x
    else:
        numbers.append(int(temp))
        temp=''
        op.append(x)
numbers.append(int(temp))

op=deque(op)
flag=True
res,idx=0,9999

for i in range(len(op)):
    if op[i]=='-':
        idx=i
        break

if idx==9999:
    print(sum(numbers))
else:
    print(sum(numbers[0:idx+1])-sum(numbers[idx+1:len(numbers)]))