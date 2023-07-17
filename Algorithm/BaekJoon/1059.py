import sys

n = int(sys.stdin.readline())
S= list(map(int,sys.stidn.readline().split()))
num = int(sys.stdin.readline())
cnt=0

for i in range(len(S)):
    for j in range(i+1,len(S)):
        if S[i]==num:
            print(0)
            break
        else:
            