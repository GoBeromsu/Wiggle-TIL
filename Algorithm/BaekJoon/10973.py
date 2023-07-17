import sys

# 1 2 3 4
# 1 2 4 3 
# 1 3 2 4
# 1 3 4 2

num = 4
numbers = [1, 2, 3, 4]

for i in range(num-1,0,-1):
    if numbers[i]>numbers[i-1]:
        for j in range(num-1,0,-1):
            if numbers[j]>numbers[i-1]:
                numbers[j],numbers[i-1]=numbers[i-1],numbers[j]
                numbers=numbers[:i]+sorted(numbers[i:],reverse=True)

if numbers == [i for i in range(num,0,-1)]:
    print(-1)
else:
    print(*numbers)