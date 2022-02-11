import sys

# fibo(n) = fibo(n-2) + fibo(n-1)
zdp = [1,0]
odp = [0,1]
for i in range(2,41):
    zdp.append(zdp[i-2]+zdp[i-1])
    odp.append(odp[i-2]+odp[i-1])

n = int(sys.stdin.readline())

for j in range(n):
    num = int(sys.stdin.readline())
    print(f"{zdp[num]} {odp[num]}")