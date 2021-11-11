
import sys

N,M = map(int,sys.stdin.readline().split())
# M,N = 13,10
count = 0
minimum = []
bB = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
wB = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
# board = ['BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','BBBBBBBBWBWBW','BBBBBBBBBWBWB','WWWWWWWWWWBWB','WWWWWWWWWWBWB']
board=[]
for n in range(N):
    board.append(sys.stdin.readline().rstrip())


for n in range(N-7):
    for m in range(M-7):
        idx1=0
        idx2=0
        for a in range(8):
            for b in range(8):
                if board[a+n][b+m]!=bB[a][b]:
                    idx1+=1
                if board[a+n][b+m]!=wB[a][b]:
                    idx2+=1
        minimum.append(idx1)
        minimum.append(idx2)

print(sorted(minimum)[0])