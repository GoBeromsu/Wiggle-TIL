import sys

# 1/1 1/2 2/1 3/1 2/2

# n : 1 2 3 4 5 6 7 8 9 10
# o : 1 2 2 3 3 3 4 4 4 4
num = int(sys.stdin.readline())

def checkLine(num):
    count=1
    min=0
    while True:
        max=count*(count+1)/2
        if(min<num and num<=max):
            return count
        min= max
        count+=1

def checkDest(num):
    sum=0
    count=1
    while True:
        sum+=count
        if(0>=(num-sum)):
            return count
        count+=1

def checkEven(num):
    if(num%2==0):
        return True
    else:
        return False

destLine=checkLine(num)
number = destLine*(destLine-1)/2
if(checkEven(destLine)):
    for i in range(num-number):

else:


print(f"checkLine : {checkLine(num)}")
print(f"checkDest : {checkDest(num)}")