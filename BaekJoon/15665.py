import sys

N,M = map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))

numbers =[]
result=[]
for i in temp:
    if not i in numbers:
        numbers.append(i)
numbers.sort()

def solve(depth,bucket):
    if depth == M:
        print(" ".join(map(str,bucket)))
        return
    for i in range(len(numbers)):
        solve(depth+1,bucket+[numbers[i]])

for n in range(len(numbers)):
    solve(1, [numbers[n]])

