import sys

# 1 2 3 4 5 666 없음
# 1 2 3 4 5 666 1의 자리 0-9
# 1 2 3 4 5 666 10의 자리 00-99
# 1 2 3 4 5 666 100의 자리 000-999

num =int(sys.stdin.readline())

name = 666
cnt=0
while(True):
    if "666" in str(name) : 
        cnt+=1
        if cnt == num : 
            print(name)
            break
    name+=1