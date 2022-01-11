import sys

N,M = map(int,sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

idx = 1

left,right = 1,max(nums)

while(left<=right):
    sum=0
    mid = (left+right)//2
    for num in nums:
        if num>mid:
            sum+=num-mid
        if sum>=M:
            break
    if sum>=M:
        left=mid+1
    else:
        right=mid-1
    
print(right)