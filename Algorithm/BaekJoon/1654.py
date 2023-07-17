import sys

K,N = map(int, sys.stdin.readline().split())
# K,N=4,11
# nums = [803,743,457,539]
nums=[]
for i in range(K):
    nums.append(int(sys.stdin.readline()))

left,right = 1,min(nums)

while left<= right:
    sum=0
    mid = (left+right)//2
    for num in nums:
        sum+=num//mid
    if sum<N:
        right= mid-1
    else:
        left = mid+1
print(right)