import sys

st = sys.stdin.readline()
answer=''
temp=''
for s in st:
    if s=='.':
        answer+='.'
        if len(temp)%4==0:
            answer+='A'*len(temp)
        else:
            m = len(temp)%4
            if m%2==1:
                print(-1)
                break
            else:
                answer+='A'*len(temp)+'B'*2
        temp=''
    temp+=s
print(answer)

