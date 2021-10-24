import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):
    arr.append(sys.stdin.readline().rstrip())


for braket in arr:
    count = 0
    idx = 0
    while 1:
        length = len(braket)

        if length == 0:
            print('YES')
            break
        elif length -1 == idx:
            print('NO')
            break 
        elif braket[idx] == '(' and braket[idx+1] == ')':
            braket = braket.replace('()','', 1)
            idx = 0
        else:
            idx+=1

