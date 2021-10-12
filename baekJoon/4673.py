
# n + n의 자리숫자들
arr =[0 for i in range(10000)]
count=1

def checkD(n:int):
    sum=n
    divValue=0
    while True:
        dLength=len(str(n))
        if(dLength==1):
            sum+=n
            break
        else:
            number= (10**(dLength-1))
            divValue=int(n/number)
            sum+=divValue
            n=n%(divValue*number)
    return sum    

for i in range(1,len(arr)+1):
    target=checkD(i)
    if (target>=10000):
        continue
    else:
        arr[target] = 1


for i in range(1,len(arr)):
    if (arr[i]!=1):
        print(i)
