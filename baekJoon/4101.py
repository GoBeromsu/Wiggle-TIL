import sys

inputs=[]
while True:
    input= list(map(int,sys.stdin.readline().split()))
    if(input[0]==0 and input[1]==0):
        break
    inputs.append(input)

for input in inputs:
    if(input[0]<=input[1]):
        print("No")
    else:
        print("Yes")