import sys

val = list(map(int,sys.stdin.readline()))
sum = 0
for i in range(len(val)):
    temp = val[i]
    if (i!=0):
        sum+=temp*(2**i)
    else:
        sum+=temp

print(sum)