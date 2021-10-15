import sys 

num = int(sys.stdin.readline())
strArr=[]
count = 0

for i in range(num):
    strArr.append(sys.stdin.readline().rstrip())

for i in range(len(strArr)):
    word= strArr[i]
    dic={}
    checkPoint=True
    for j in range(1,len(word)):
        if(word[j-1]==word[j]):
            if(j==1):
                dic[word[j-1]]=1
            dic[word[j]] +=1
        elif(word[j] in dic.items()):
            continue
        else:
            dic[word[j]]=1
    for key,value in dic.items():
        if(word.count(key)!=value):
            checkPoint=False
            break
    if(checkPoint is True):
        count+=1
print(count)