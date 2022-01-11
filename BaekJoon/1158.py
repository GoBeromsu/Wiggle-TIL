import sys

N,M = map(int, sys.stdin.readline().split())

arr =[i for i in range(1,N+1)]
arr.sort(reverse=True)
stack = []

print('<',end='')
while arr:
    for i in range(M-1):
        arr.insert(0, arr.pop())
        # print(arr)


    
    if len(arr)==1:
        print(arr.pop(),end='')
    else:
        print(arr.pop(),end=', ')

print('>')

# 1 2 3 4 5 6 7
# 1 2   4 5 6 7
# 1 2 4 5   7