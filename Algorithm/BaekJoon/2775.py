import sys

num = int(sys.stdin.readline())
floor=0
room =0
arr=[]
memo_list= [[None]*15 for i in range(15)]

def destNum(floor,room):
    if(memo_list[floor][room] is not None):
        return memo_list[floor][room]
    if(floor==0):
        return room
    else:
        dest=0
        for i in range(1,room+1):
            memo_list[floor-1][i] =destNum(floor-1,i)
            dest += memo_list[floor-1][i]
        memo_list[floor][room] = dest
        return memo_list[floor][room]

for i in range(num):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    arr.append([floor,room])
for j in range(num):
    print(destNum(arr[j][0],arr[j][1]))