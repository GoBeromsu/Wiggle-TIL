import sys

st = sys.stdin.readline().rstrip()
stl = []

def setEmpty(st,temp):
    if temp!='' and temp[0]!=st:
        stl.append(temp)
        temp=''
    return temp

def solve(st):
    answer=''
    temp=''
    
    for s in st:
        if temp=='':
            temp+=s
        elif temp[0]==s:
            temp+=s
        else:
            stl.append(temp)
            temp=s
    stl.append(temp)
    if len(st)==0:
        return -1
    # if len(stl)==1 and stl[0][0]=='.':
    #     return -1
    for st in stl:
        if st[0]=='X':
            if len(st)%2!=0:#짝수가 아닌 것은 만들 수 없으니까 제거 한다
                return -1
            x = len(st)//4
            y= len(st)-x*4
            answer+='A'*x*4
            answer+=y*'B'
        else:
            answer+=len(st)*'.'
    return answer

print(solve(st))