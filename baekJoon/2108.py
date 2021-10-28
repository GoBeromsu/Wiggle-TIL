import sys


dic = {}
num = int(sys.stdin.readline())

for n in range(num):
    val = int(sys.stdin.readline())
    if val in dic:
        dic[val]+=1
    else:
        dic[val]=1

dicLength = len(dic)


def avg():
    sum=0
    for key,value in dic.items():
        sum+=key*value
    print(round(sum/num))


def center():
    cnt=0
    center= (num//2)+1  
    for key,value in sorted(dic.items()):
        for n in range(value):
            cnt+=1
            if(center==cnt):
                print( key)
                
        
def numRange():
    sortedDic=sorted(dic)
    print(abs(sortedDic[-1]-sortedDic[0]))
def mini():
    sortedDic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    if len(dic)==1 or sortedDic[0][1] != sortedDic[1][1]:
        print(sortedDic[0][0])
    else:
        minval = sortedDic[0][1]
        arr = []
        for key,value in sortedDic:
            if value == minval:
                arr.append(key)
        arr.sort()
        print(arr[1])

avg()
center()
mini()
numRange()