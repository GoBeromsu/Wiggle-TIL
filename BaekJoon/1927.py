import sys
import heapq
num = int(sys.stdin.readline())
numbers = []

for i in range(num):
    n=int(sys.stdin.readline())
    if n==0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, n)