import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
num = [i for i in range(1,n+1,1)]
checkNum=[i for i in num]
checkNum.sort(reverse=True)

print(*num)

def solve(numbers:list):
    x,y=0,0
    for i in range(n-1,0,-1):
        if numbers[i]>numbers[i-1]:
            x,y= i-1,i
            break
    for i in range(n-1,0,-1):
        if numbers[x]<numbers[i]:
            numbers[x],numbers[i] = numbers[i],numbers[x]
            break
    numbers = numbers[:y]+sorted(numbers[y:])
    if checkNum == numbers:
        print(*numbers)
        return
    else:
        print(*numbers)
        solve(numbers)
solve(num)