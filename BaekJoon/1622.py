import sys

def check(A,B):
    arr=[]
    result=[]
    temp=''
    for a in A:
        if a in B:
            temp+=a
        else:
            arr.append(temp)
            temp=''
    if temp:
        arr.append(temp)
    temp=''
    maxLen=0
    for a in arr:
        if len(a)>maxLen:
            maxLen=len(a)
    for a in arr:
        if len(a)==maxLen:
            result.append(a)
    result.sort()
    for r in result:
        temp+=r
    return temp

while 1:
    a= sys.stdin.readline().rstrip()
    b= sys.stdin.readline().rstrip()
    if not a and not b:
        break
    print(check(a, b))
