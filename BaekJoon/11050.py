import sys

inputs = list(map(int,sys.stdin.readline().split()))
memoiztion = {}
n = inputs[0]
k = inputs[1]

def fac(num):
    if num in memoiztion:
        return memoiztion[num]
    if(num==1 or num==0):
        memoiztion[num]=1   
        return memoiztion[num]     
    else:
        memoiztion[num] = fac(num-1)*num
        return memoiztion[num]
print(int(fac(n)/(fac(k)*fac(n-k))))