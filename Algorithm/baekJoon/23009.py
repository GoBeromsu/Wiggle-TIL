import sys

# 난쟁이는 7명, 거짓말쟁이 2명 섞여 있음 

high = [int(sys.stdin.readline()) for _ in range(9)]
total = sum(high)

for i in range(9):
    for j in range(i+1,9):
        num1 = high[i]
        num2 = high[j]
        if total-(num1+num2) == 100:
            high.remove(num1)
            high.remove(num2)
            high.sort()
            for h in high:
                print(h)
            break
    if len(high)<9:
        break
