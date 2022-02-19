import sys

n,m = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))


def calc(start,end):
    global numbers
    sum=0
    if start==end:
        print(numbers[start-1])
        return
    else:
        for i in range(start-1,end):
            sum+=numbers[i]
    print(sum)
    return

for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    calc(start,end)