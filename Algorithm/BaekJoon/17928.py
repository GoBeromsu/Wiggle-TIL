import sys

num = int(sys.stdin.readline())
N = list(map(int,sys.stdin.readline().split()))
# num =4
# N = [3,5,2,7]
stack = []
result = [-1 for i in range(num)]

for i in range(0,num-1):
    stack.append(i)
    while stack and N[stack[-1]]<N[i+1]:
        result[stack.pop()]=N[i+1]

print(*result)