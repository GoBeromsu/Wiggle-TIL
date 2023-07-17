import sys

n, m = map(int, sys.stdin.readline().split())
nset = set()
mset = set()
for i in range(n):
    nset.add(sys.stdin.readline().rstrip())
for j in range(m):
    mset.add(sys.stdin.readline().rstrip())

result = list(nset.intersection(mset))

print(len(result))
for r in sorted(result):
    print(r)
