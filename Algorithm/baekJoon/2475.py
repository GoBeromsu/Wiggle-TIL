import sys

inputs=list(map(int,sys.stdin.readline().split()))

prNum = 0

for input in inputs:
    prNum+=pow(input,2)
print(prNum%10)