import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(n)]
m = max(numbers)
arr = [False,False]+[True]*(max(numbers)-1)

def checkPrime(num):
    n = int(num **0.5)+1
    for i in range(2,n):
        for j in range(i*2,num,i):
            arr[j]=False

checkPrime(m)
for num in numbers:
    cnt=0
    for i in range((num//2)+1):
        if arr[i] and arr[num-i]:
            cnt+=1
    print(cnt)
