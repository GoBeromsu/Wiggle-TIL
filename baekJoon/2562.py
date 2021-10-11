import sys

arr=[]
for i in range(9):
    arr.append(int(sys.stdin.readline()))

max = arr[0]
index = 0

for i in range(9):
    if(arr[i]>max):
        max = arr[i]
        index=i

print(max)
print(index+1) 
