import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    n = int(sys.stdin.readline())
    if n==0:
        arr.pop()
    else:
        arr.append(n)

print(sum(arr))