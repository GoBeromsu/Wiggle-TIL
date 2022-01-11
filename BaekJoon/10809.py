import sys

val = sys.stdin.readline().rstrip()
a = 97
arr=[-1 for i in range(26)]

for i in range(len(val)):
    for j in range(a,a+26):
        if (val[i]==chr(j)and arr[j-a]==-1):
            arr[j-a]=i
        

for i in range(len(arr)):
    print(arr[i], end=' ')