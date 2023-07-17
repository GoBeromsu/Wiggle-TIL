import sys
import math

x= int(sys.stdin.readline())

a = int(x/10)
b = x%10

count=0

while True:
    c= a+b
    a=b
    b=c%10
    newNum = a*10+c%10
    count+=1
    if (newNum==x):
        break

print(count)