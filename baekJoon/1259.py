import sys
import math

arr = []

while True:
    input = int(sys.stdin.readline())
    if input == 0:
        break
    arr.append(input)

for i in range(len(arr)):
    stNum = str(arr[i])
    stRange = int(len(stNum) / 2)
    if(len(stNum)==1):
        print("yes")
        continue
    for j in range(0, stRange):
        if int(stNum[j]) != int(stNum[-j - 1]):
            print("no")
            break
        else:
            if j + 1 == stRange:
                print("yes")
