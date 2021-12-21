import sys

num = int(sys.stdin.readline())
digit = len(str(num))
count = 0
if digit==1:
    print(num)
else:
    count = 9
    for i in range(2,digit+1,1):
        if i == digit:
            count+=i*(num-10**(i-1)+1)
            break
        else:
            count+=i*(9*10**(i-1))
    print(count)