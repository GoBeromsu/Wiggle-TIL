import sys

num = int(sys.stdin.readline())
count=0

def getGap(num):
    gap=0
    nums=[]
    arr=[]
    stNum= str(num)
    
    for i in range(len(stNum)):
        nums.append(int(stNum[i]))
    arrLength=len(nums)
    if (arrLength==1):
        arr.append(1)
    else:
        for i in range(arrLength-1):
            arr.append(nums[i]-nums[i+1])
    temp = list(set(arr))
    return temp

for i in range(1,num+1):
    if(len(getGap(i))==1):
        count+=1
print(count)