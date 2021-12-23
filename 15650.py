import sys

def dfs(start:int,n:int,m:int,result:list):
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in range(start,n+1):
        if i not in result:
            result.append(i)
            dfs(i,n, m, result)
            result.pop()
n,m = map(int,sys.stdin.readline().split())
dfs(1,n, m, [])