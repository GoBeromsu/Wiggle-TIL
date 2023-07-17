import sys

num = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
x,y = 0,0
for i in range(num-1,0,-1):
    if numbers[i]>numbers[i-1]:
        x,y= i-1,i
        break
for i in range(num-1,0,-1):
    if numbers[x]<numbers[i]:
        numbers[x],numbers[i] = numbers[i],numbers[x]
        break
numbers = numbers[:y]+sorted(numbers[y:])
if numbers == [i for i in range(1,num+1)]:
    print(-1)
else:
    print(*numbers)