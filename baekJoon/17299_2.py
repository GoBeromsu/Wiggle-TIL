import sys

result = [-1 for i in range(int(sys.stdin.readline()))]
arr = list(map(int, sys.stdin.readline().split()))
dic={}
stack = []
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for s in enumerate(arr):
    while stack and dic[arr[stack[-1]]]<dic[s[1]]:
        result[stack.pop()]=s[1]
    stack.append(s[0])

print(*result)