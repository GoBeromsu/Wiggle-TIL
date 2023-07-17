import sys

n = int(sys.stdin.readline())

for _ in range(n):
    number = int(sys.stdin.readline())
    if number==0:
        print(0)
        continue
    
    clothes=dict()
    for _ in range(number):
        clo_name,clo_type=map(str,sys.stdin.readline().split())
        if clo_type in clothes.keys():
            clothes[clo_type]+=1
        else:
            clothes[clo_type]=1

        cnt=1
        for key in clothes.keys():
            cnt*=clothes[key]+1
    print(cnt-1)