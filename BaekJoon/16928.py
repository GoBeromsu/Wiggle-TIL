import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

mp = [0 for i in range(101)]
check = [0 for _ in range(101)]
ans = []
for i in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    mp[x] = y
    check[x] = 1

# 참 : 사다리, 거짓 : 뱀

