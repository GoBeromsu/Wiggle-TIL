# n + n의 자리숫자들
arr =[0 for i in range(10000)]

def checkD(n:int):
    sum=0
    dLength=len(str(n))
    for i in range(dLength,0,-1):
        temp=n/(dLength**i)
        sum=+temp
        # remain=n-temp*dLength**i

