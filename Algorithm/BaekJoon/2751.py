import sys

num = int(sys.stdin.readline())
arr = []
for i in range(num):
    arr.append(int(sys.stdin.readline()))

for n in sorted(arr):
    print(n)