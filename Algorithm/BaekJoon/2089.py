import sys

num =int(sys.stdin.readline())

if num ==0:
    print(0)

result =[]
while num:
    if num %2==1:
        result.append(1)
        num = num//-2+1
    else:
        result.append(0)
        num = num//-2

while result:
    print(result.pop(),end='')