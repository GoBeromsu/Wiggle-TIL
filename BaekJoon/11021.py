N = int(input())
arr = []

for n in range(0,N):
    value=input().split()
    a = int(value[0])
    b = int(value[1])
    arr.append( a+b)


for i in range(0,N):
    print("Case #{}: {}".format(i+1,arr[i]))