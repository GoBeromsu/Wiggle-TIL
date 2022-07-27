import sys
import heapq


num = int(sys.stdin.readline())
heap = []
ds = 0
for n in range(num):
    nm = int(sys.stdin.readline())
    if n==0:
        ds=nm
    else:
        heapq.heappush(heap, -nm)
count = 0
while heap:
    max = -heapq.heappop(heap)
    if ds>max:
        break
    ds+=1
    heapq.heappush(heap,-max+1)
    count+=1

print(count)

