import sys
import math
inputs = list(map(int,sys.stdin.readline().split()))

a=inputs[0]
b=inputs[1]
v=inputs[2]

n=math.ceil((v-b)/(a-b))

print(n)