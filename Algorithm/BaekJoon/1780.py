import sys


def solve(x,y,n):

    num = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if (paper[i][j]!=num):
                for k in range(3):
                    for l in range(3):
                        solve(x+k*n//3, y+l*n//3, n//3)
                return
    plus(ㅋ)
def plus(num):
    global a,b,c
    if num ==-1:
        a+=1
    elif num==0:
        b+=1
    else:
        c+=1 

N = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
a,b,c=0,0,0

solve(0,0,N)

for cnt in (a,b,c):
    print(cnt)