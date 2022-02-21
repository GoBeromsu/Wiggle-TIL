import sys

# 회의 i에 대해 시작 시간과 끝나는 시간이 주어져 있다.
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
# 회의는 한 번 시작하면 중간에 중단 될 수 없음
# 한 회의가 끝나는 것과 동시에 다음 회의 시작될 수 있다.
# 시작시간과 끝나는 시각이 같을 수 있음

time = int(sys.stdin.readline())
conference = [list(map(int,sys.stdin.readline().split())) for _ in range(time)]
mx=0
def con(idx):
    count=0
    start,end=idx[0],idx[1]
    while 1:
        for i in time:
            if i[0]== end+1:
                count+=1
                start,end=i[0],i[1]


for i in conference:
    mx = max(mx,con(i))
print(mx)