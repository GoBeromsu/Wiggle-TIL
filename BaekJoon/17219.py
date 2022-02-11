import sys

n,m = map(int,sys.stdin.readline().split())

dic = {}

for i in range(n):
    web,key = map(str,sys.stdin.readline().rstrip().split())
    dic[web] = key
for j in range(m):
    w = sys.stdin.readline().rstrip()
    print(dic[w])