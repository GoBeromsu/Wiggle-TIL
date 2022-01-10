import sys


N = int(sys.stdin.readline())
consult = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result=0
def solve(day,fee):
    global result,consult
    if day==N:
        result=max(fee,result)
        return
    if day>N:
        return
    solve(day+consult[day][0], fee+consult[day][1])
    solve(day+1, fee)
solve(0 , 0)
print(result)