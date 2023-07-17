import sys

inputs= list(map(int,sys.stdin.readline().split()))

index = 0
for i in range(len(inputs)):
    min=1000000001
    for j in range(i,len(inputs)):
        if(min>inputs[j]):
            min=inputs[j]
            index=j
    temp = inputs[i]
    inputs[i] = min
    inputs[index] = temp
for i in inputs:
    print(i, end=" ")
