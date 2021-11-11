import sys

def bnSearch(num:int,aList:list):
    start=0
    end=len(aList)-1
    while(start<=end):
        mid = int((start+end)/2)
        if(num>aList[mid]):
            start = mid+1
        elif(num<aList[mid]):
            end=mid-1
        elif(num==aList[mid]):
            return 1
    return 0

arr = []      
for i in range(2):
    num = int(sys.stdin.readline())
    arr.append(list(map(int,sys.stdin.readline().split())))

arr[0]=sorted(arr[0])
for num in arr[1]:
    print(bnSearch(num, arr[0]))
