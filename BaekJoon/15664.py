import sys

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

numbers.sort()
dCheck=[]

def solve(result:list,idx):
    if len(result) == M:
        if result in dCheck:
            return
        dCheck.append(result)
        return
    for i in range(idx+1,N):
        solve(result+[numbers[i]], i)

for i in range(N):
    solve([numbers[i]],i)

for i in dCheck:
    for j in range(len(i)):
        print(i[j],end=' ')
    print()