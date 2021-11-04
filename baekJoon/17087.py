import sys

D = []
N,S = map(int, sys.stdin.readline().split())
A= list(map(int,sys.stdin.readline().split()))

def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

for a in range(len(A)):
    D.append(abs(S-A[a]))

result = D[0]
for d in range(1,len(D)):
    result = gcd(D[d], result)
print(result)