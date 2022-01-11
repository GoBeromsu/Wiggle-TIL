import sys

num = int(sys.stdin.readline())
arr = []

def strPop(string):
    arr =list(map(str, string))
    while len(arr)>1:
        print(arr.pop(),end='')
    print(arr.pop(),end=' ')
    
for i in range(num):
    sentence = list(map(str,sys.stdin.readline().split()))
    for val in sentence:
        strPop(val)
    print()
