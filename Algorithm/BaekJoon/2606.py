import sys

num = int(sys.stdin.readline())
net = int(sys.stdin.readline())

mp = [False for _ in range(101)]
computers = [set() for i in range(101)]
cnt=0
for i in range(net):
    n1,n2 = map(int,sys.stdin.readline().split())
    computers[n1].add(n2)
    computers[n2].add(n1)
for i in range(1,num+1):
    computers[i] = list(computers[i])

def bfs(com,node):
    global computers
    if mp[node]==True:
        return 
    else:
        mp[node] = True
        for i in com:
            bfs(computers[i], i)

bfs(computers[1], 1)
for i in mp:
    if i:
        cnt+=1
print(cnt-1)