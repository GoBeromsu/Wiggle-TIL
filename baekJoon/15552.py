import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    inputs=sys.stdin.readline().split()
    a=int(inputs[0])
    b=int(inputs[1])
    arr.append(a+b)

for i in range(num):
    print(arr[i])