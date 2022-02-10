import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}
li = []
for n in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    dic[name] = n
    li.append(name)
for m in range(M):
    i = sys.stdin.readline().rstrip()
    if i.isalpha():
        print(dic[i])
    else:
        print(li[int(i)-1])
