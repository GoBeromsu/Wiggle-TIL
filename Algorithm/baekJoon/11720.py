import sys

sum=0
n = int(sys.stdin.readline())

nString= sys.stdin.readline().rstrip()

for i in range(n):
    sum+=int(nString[i])
print(sum)