import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

answer,i,count=0,0,0

while i<m-1:
    if s[i:i+3]=='IOI':
        i+=2
        count+=1
        if count ==n:
            answer+=1
            count -=1
    else:
        i+=1
        count=0
print(answer)