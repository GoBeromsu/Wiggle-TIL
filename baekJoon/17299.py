import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

stack = []
result = [-1 for i in range(N)]
dic={}

for a in arr:
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1


for i in range(0,N-1):
    stack.append(i)
    while stack and dic[arr[stack[-1]]]<dic[arr[i+1]]:
        result[stack.pop()] = arr[i+1]      

print(*result)