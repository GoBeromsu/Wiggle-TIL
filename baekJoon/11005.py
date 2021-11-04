import sys

dic ={i:i for i in range(10)}
for i in range(10,36):
    dic[i] = chr(i+55)
result=[]
N,B = map(int, sys.stdin.readline().split())
while N:
    r = N%B
    q = (N-r)//B
    if r:
        result.append(dic[r])
    else:
        result.append(0)
    N=N//B

while result:
    print(result.pop(),end='')