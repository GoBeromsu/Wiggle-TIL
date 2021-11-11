import sys

inputs = list(map(int,sys.stdin.readline().split()))

dscList = [8, 7, 6, 5, 4, 3, 2, 1]
ascList=sorted(dscList)

if (inputs==ascList):
    print("ascending")
elif(inputs==dscList):
    print("descending")
else:
    print("mixed")