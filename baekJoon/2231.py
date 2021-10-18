import sys

input = int(sys.stdin.readline())

def mkNum(num):
    arr = []
    stNum=str(num)
    sum=num
    for i in range(len(stNum)):
        sum+=int(stNum[i])
    return sum

for i in range(input):
    if(mkNum(i)==input):
        print(i)
        break
    elif(input==i+1):
        print(0)