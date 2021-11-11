import sys

fac = [1,1]+[0]*499
cnt = 0
def fact(n):
    if fac[n] != 0:
        return fac[n]
    else:
        fac[n] = n * fact(n-1)
        return fac[n]
n = fact(int(sys.stdin.readline().rstrip()))
arr = list(map(int,str(n)))

for _ in range(len(arr)):
    if arr.pop() == 0:
        cnt+=1
    else:
        print(cnt)
        break