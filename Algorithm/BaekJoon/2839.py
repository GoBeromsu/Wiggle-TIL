import sys

num = int(sys.stdin.readline())
arr=[]

for i in range(int(num/3)+1):
    shareFive= (num-3*i)/5
    if(shareFive.is_integer()):
        arr.append(shareFive+i)
    else:
        continue

arr = sorted(arr)
if(len(arr)==0):
    print(-1)
else:
    print(int(arr[0]))