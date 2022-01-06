import sys

N,M = map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))
numbers=list(dict.fromkeys(temp))
numbers.sort()

def solve(depth,result):
    if depth == M:
        print(" ".join(map(str,result)))
        return
    for i in numbers:
        if result[depth-1] <= i: 
            solve(depth+1, result+[i])

for i in numbers:
    solve(1, [i])