import sys

n = int(sys.stdin.readline())
m = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
]
wcount,bcount =0, 0

def rec(x,y,n):
    global wcount,bcount,m
    color = m[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != m[i][j]:
                rec(x, y, n//2)
                rec(x, y+n//2, n//2)
                rec(x+n//2, y, n//2)
                rec(x+n//2, y+n//2, n//2)
                return
    if color==0:
        wcount+=1
    else:
        bcount+=1

rec(0, 0, n)
print(wcount)
print(bcount)