N = int(input())
arr = [[0] *3 for j in range(N)]

for n in range(0,N):
    value=input().split()
    a = int(value[0])
    b = int(value[1])
    arr[n][0] = a
    arr[n][1] = b
    arr[n][2] = a+b


for i in range(0,N):
    print("Case #{}: {} + {} = {}".format(i+1,arr[i][0],arr[i][1],arr[i][2]))