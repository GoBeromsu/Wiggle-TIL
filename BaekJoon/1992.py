import sys
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())

tree = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
ans=[]
def solve(x,y,length):
    global ans
    node = tree[x][y]

    for i in range(x,x+length):
        for j in range(y,y+length):
            if node!=tree[i][j]:
                ans.append("(")
                quad=length//2
                solve(x, y, quad)
                solve(x, y+quad, quad)
                solve(x+quad, y, quad)
                solve(x+quad, y+quad, quad)
                ans.append(")")
                return
    ans.append(node)
solve(0, 0, n)
print("".join(map(str,ans)))

import