import sys

num=1
numArr= []

for i in range(3):
    num= num*int(sys.stdin.readline())
numLength=len(str(num))

for i in range(10):
    numArr.append(0)

arr = list(map(int,list(str(num))))

for i  in range(numLength):
    numArr[arr[i]]+=1

for i in numArr:
    print(i)
print()