import sys

time = int(sys.stdin.readline())
conference = [list(map(int,sys.stdin.readline().split())) for _ in range(time)]

conference = sorted(conference,key=lambda x:[x[1],x[0]])

mx=0
start=0

for c in conference:
    if c[0] >= start:
        start= c[1]
        mx+=1
print(mx)