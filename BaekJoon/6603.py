import sys
from itertools import combinations

numbers=[]
while 1:
    num = list(map(int,sys.stdin.readline().split()))
    if num[0]==0:
        break
    else:
        numbers.append(num[1:])
for i in range(len(numbers)):
    for n in combinations(numbers[i],6):
        print(*n)
    print()