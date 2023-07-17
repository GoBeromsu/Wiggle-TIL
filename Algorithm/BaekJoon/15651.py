import sys

def dfs(n:int,m:int,result:list):
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in range(1,n+1):
        result.append(i)
        dfs(n, m, result)
        result.pop()
n,m = map(int,sys.stdin.readline().split())
dfs(n, m, [])