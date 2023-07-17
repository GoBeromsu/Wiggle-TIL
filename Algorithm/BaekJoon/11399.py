import sys

N = int(sys.stdin.readline())
p=list(map(int,sys.stdin.readline().split()))
p.sort()
cnt=0

for i in range(N):
    cnt+=p[i]*(N-i)
print(cnt)