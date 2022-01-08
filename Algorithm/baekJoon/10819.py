import sys,itertools

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

result=0
for num in itertools.permutations(numbers):
    maximum=0
    for i in range(n-1):
        maximum+=abs(num[i]-num[i+1])
    if result<maximum:
        result=maximum
    # print(maximum)
print(result)