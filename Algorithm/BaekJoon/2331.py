import sys

A,P=map(int,sys.stdin.readline().split())

def calc(number):
    ans=0
    numbers = list(map(int,str(number)))
    for i in numbers:
        ans+=i**P
    return ans

D=[A]
idx=0
while 1:
    number = calc(D[-1])
    if number in D:
        idx=D.index(number)
        break
    else:
        D.append(number)
print(idx)
