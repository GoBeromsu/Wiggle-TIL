import sys

st = sys.stdin.readline().rstrip()
stl=[]
temp=''
flag=st[0]
for s in st:
    if flag!=s:
        stl.append(temp)
        temp=s
        flag=s
    else:
        temp+=s
stl.append(temp)

zcount=0
ocount = 0
for st in stl:
    if st[0]=='0':
        zcount+=1
    else:
        ocount+=1
print(min(zcount,ocount))