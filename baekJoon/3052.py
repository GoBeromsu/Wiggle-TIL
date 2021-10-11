import sys

divNum =42
arr=[]
count=0
for i in range(10):
    temp= int(sys.stdin.readline())
    arr.append(temp%42) 


for i in range(0,len(arr)):
    if (arr[i] is None):
        continue
    for j in range(i+1,len(arr)):
        if((i+1)==len(arr)):
            continue
        if (arr[i]==arr[j]):
            arr[j]= None

for i in range(0,len(arr)):
    if(arr[i] is not None):
        count+=1
print(count)