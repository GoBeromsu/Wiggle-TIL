import sys

# dic = {55:185,58:183,88:186,60:175,46:155}
dic = []
num = int(sys.stdin.readline())

for n in range(num):
    x,y = map(int,sys.stdin.readline().split())
    dic.append([x,y])

for i in dic:
    cnt = 1
    for j in dic:
        # print(f"{i[0]}: {i[1]}  {j[1]}")
        if i==j:
            continue
        else:
            if(i[0]<j[0] and i[1]<j[1]):
                cnt+=1
    print(cnt,end=' ')



