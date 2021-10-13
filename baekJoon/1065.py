import sys

num = sys.stdin.readline().strip()
numArr=[]

for i in range(len(num)):
    numArr.append(int(num[i]))

def getGap(numArr:list):
    gap=0
    arrLength=len(numArr)
    arr=[]
    for i in range(1,arrLength):
        if (arrLength==1):
            return arr[0].append(1)
        arr[i].append(num[i-1]-num[i])
    return list(set(arr))

print(getGap(121))