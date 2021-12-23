import sys

n,m = map(int,sys.stdin.readline().split())
numbers = [i for i in range(1,n+1)]
result=[]
def dfs():
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    for number in numbers:
        if number not in result:
            result.append(number)
            dfs()
            result.pop()
dfs()
