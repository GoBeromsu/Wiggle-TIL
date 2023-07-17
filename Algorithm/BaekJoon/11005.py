import sys

dic ={f"{i}":i for i in range(10)}
for i in range(10,36):
    dic[chr(i+55)] = i
sum=0
N,B = sys.stdin.readline().split()
N = list(N)
for i in range(len(N)):
    sum+=dic[N.pop()]*(int(B)**i)

print(sum)