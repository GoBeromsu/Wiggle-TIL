import sys
from itertools import permutations
N,M=map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()

for n in permutations(numbers, M):
    print(*n)