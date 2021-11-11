import sys

decimal = [False,False]+[True]*999999

for i in range(2,1001):
    if decimal[i]==True:
        for j in range(i*2,1000001,i):
            decimal[j]=False

while 1:
    n = int(sys.stdin.readline())
    if n ==0:
        break

    a=0
    b=n
    for _ in range(1000000):
        if decimal[a] and decimal[b]:
            print(f"{n} = {a} + {b}")
            break
        a+=1
        b-=1
        
    else:
        print("Goldbach's conjecture is wrong.")
        break