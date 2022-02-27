import sys
import heapq

n = int(sys.stdin.readline())
heap=[]
for i in range(n):
    num=int(sys.stdin.readline())
    if num ==0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(num),num))