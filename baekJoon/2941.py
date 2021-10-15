import sys

dic ={'c=':1,'c-':1,'dz=':2,'d-':1,'lj':1,'nj':1,'s=':1,'z=':1}
input =sys.stdin.readline().rstrip()

strLength = len(input)

for key in dic:
    valCount = input.count(key)
    if(input.rfind(key)!=-1):
        strLength=strLength-(dic[key]*valCount)

if ('dz=' in input and 'z=' in input):
    strLength+=(input.count('dz='))
print(strLength)
