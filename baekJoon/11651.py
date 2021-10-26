import sys

arr = []
num = int(sys.stdin.readline())

for i in range(num):
    x, y = map(int,sys.stdin.readline().split())
    arr.append([y,x])

for i in sorted(arr):
    print(f"{i[1]} {i[0]}")