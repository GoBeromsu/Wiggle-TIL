import sys

num = int(sys.stdin.readline())
arr=[]
floor=0
room=0
for i in range(num):
    arr.append( list(map(int,sys.stdin.readline().split())))
for j in range(num):
    floor=arr[j][2]%arr[j][0]
    room=int(arr[j][2]/arr[j][0])+1
    if(floor==0):
        floor=arr[j][0]
        room=room-1
    if(room<10):
        print(f"{floor}0{room}")
    else:
        print(f"{floor}{room}")
