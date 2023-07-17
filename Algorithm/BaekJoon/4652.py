import sys

inputs=[]
num = int(sys.stdin.readline())
for i in range(num):
    input= list(map(int,sys.stdin.readline().split()))
    inputs.append(input)

for input in inputs:
    if(input[0]>=input[1]):
        print("MMM BRAINS")
    else:
        print("NO BRAINS")