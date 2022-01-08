import sys
# n개의 나라
# w[i][j]는 i에서 j가는데 드는 비용
# 여행 갔던 나라로 다시 돌아와야함

n = int(sys.stdin.readline())
w = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
minimum= sys.maxsize

def travel(home:int,start:int,fee:int,checkW:list):
    global minimum
    if len(checkW)==n and w[start][home]!=0:
        minimum=min(minimum, fee+w[start][home])
        return
    for i in range(n):
        if w[start][i]!=0 and i not in checkW and fee<minimum:
            checkW.append(i)
            travel(home,i, fee+w[start][i],checkW)
            checkW.pop()
for i in range(n):
    travel(i,i,0, [i])
print(minimum)
