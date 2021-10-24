import sys

dic ={0:-1,1:-1}
num = int(sys.stdin.readline())
count = 0
for i in range(2,1001):
    dic[i]=1
    
for number in range(2,1001):
    for key,value in dic.items():
        if value == -1:
            continue
        if(key%number==0 and key!=number):
            dic[key]=-1


numbers = list(map(int,sys.stdin.readline().split()))

for number in numbers:
    if dic[number]==1:
        count+=1
print(count)