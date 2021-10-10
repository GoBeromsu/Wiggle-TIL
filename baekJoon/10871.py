NX = input().split()
N =  int(NX[0])
x = int(NX[1])

num = list(map(int,input().split()))
arr = ""

for n in range(N):
    if (num[n]<x):
        arr += str(num[n])+" "

print(arr)