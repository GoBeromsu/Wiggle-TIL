import sys

dic = {}

N = int(sys.stdin.readline())

nList = list(map(int,sys.stdin.readline().split()))

for i in nList:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

M = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))

for j in mList:
    if j in dic:
        print(dic[j],end=' ')
    else:
        print("0",end=" ")
