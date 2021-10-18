import sys

inputs = list(map(int,sys.stdin.readline().split()))

for i in range(1,len(inputs)):
    gap = inputs[0] - inputs[1]
    if((inputs[i-1]-inputs[i]!=gap)):
        print("mixed")
        break
    elif(gap<0):
        print("ascending")
        break
    else:
        print("descending")
        break