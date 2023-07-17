import sys

N,M,B = map(int, sys.stdin.readline().split())
mp = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
time,height= sys.maxsize,0

for h in range(257):
    bot,top=0,0
    for i in range(N):
        for j in range(M):
            if mp[i][j] <h:
                bot+=h-mp[i][j]
            else:
                top += mp[i][j]-h
    if bot>top+B:
        continue
    t= bot +top*2
    if t<=time:
        time=t
        height=h
print(time,height)