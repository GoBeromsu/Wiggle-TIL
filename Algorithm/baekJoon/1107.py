import sys

input = sys.stdin.readline
dest = int(input())
ans = abs(100 - dest)
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - dest))
print(ans)
