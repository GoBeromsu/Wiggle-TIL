import sys

M,N = map(int, sys.stdin.readline().split())

arr = [False,False] + [True] * (N-1)

for i in range(2,N+1):
    for j in range(2*i,N+1,i):
        arr[j] = False

for i in range(M,N+1):
    if arr[i] == True:
        print(i)