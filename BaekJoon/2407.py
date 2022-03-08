import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
numbers = [0 for i in range(101)]
numbers[1], numbers[2] = 1, 2
for i in range(3, n + 1):
    numbers[i] = numbers[i - 1] * i

print(numbers[n] // (numbers[m] * numbers[n - m]))

