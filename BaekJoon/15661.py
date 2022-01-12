import sys
from itertools import combinations
N = int(sys.stdin.readline())
# S = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
S=[list(map(int, sys.stdin.readline().split())) for i in range(N)]
members=[i for i in range(N)]
minVal=sys.maxsize

for i in range(1,N//2+1):
    member_divived = combinations(members, i)
    for x in member_divived:
        s_list=list(x)
        l_list = list(set(members)-set(s_list))
        s_Asum,l_Asum=0,0
        for j in range(N-1):
            for k in range(N-1):
                try:
                    s_sum=S[s_list[j]][s_list[k]]
                except IndexError:
                    s_sum=0
                try:
                    l_sum=S[l_list[j]][l_list[k]]
                except IndexError:
                    l_sum=0
                s_Asum+=s_sum
                l_Asum+=l_sum
        minVal=min(minVal, abs(s_Asum-l_Asum))
print(minVal)