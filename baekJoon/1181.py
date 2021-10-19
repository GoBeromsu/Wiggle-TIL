import sys


arr = []
num = int(sys.stdin.readline())

for i in range(num):
    word = sys.stdin.readline().rstrip()
    if word not in arr:
        arr.append(word)
arr.sort(key=len)

if(len(arr[0])==len(arr[-1])):
    for word in sorted(arr):
        print(word)
else:
    length = len(arr[0])
    idx=0
    for j in range(0,len(arr)):
        if(length!=len(arr[j])):
            for word in sorted(arr[idx:j]):
                print(word)
            idx=j
            length=len(arr[j])
        if(j+1==len(arr)):
            for word in sorted(arr[idx:]):
                print(word)