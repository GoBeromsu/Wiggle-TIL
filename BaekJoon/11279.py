import sys
import heapq

# 배열에 자연수를 x를 넣는다
# 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다

n = int(sys.stdin.readline())
l = []

for i in range(n):
    t= int(sys.stdin.readline())
    if t == 0:
        if not l:
            print(0)
        else:
            print(heapq.heappop(l)[1])
    else:
        heapq.heappush(l, (-t,t))
