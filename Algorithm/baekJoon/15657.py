import sys


n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
result = []
finalResult = []

def dfs(n, m, numbers,result):
    if len(result) == m:
        finalResult.append(tuple(result))
        return
    for num in numbers:
        result.append(num)
        dfs(n, m, numbers,result)
        result.pop()

dfs(n, m, numbers, result)
for num in list(set(finalResult)):
    print(' '.join(map(str,num)))