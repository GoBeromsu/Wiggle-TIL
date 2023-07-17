import sys

num = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

if len(numbers)==1:
    print(numbers[0]**2)
else:
    numbers.sort()
    print(numbers[0]*numbers[-1])