import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    inputs= list(map(str,sys.stdin.readline().split()))
    arr.append(inputs)


for i in range(n):
    outString=""
    mulNum = int(arr[i][0])
    for j in range(len(arr[i][1])):
        outString+=mulNum*arr[i][1][j]
    print(outString)

