import sys

dic = {chr(key):0 for key in range(97,123)}
exp = list(sys.stdin.readline().rstrip())
# exp=list('baekjoon')

for s in exp:
    dic[s]+=1

for k in dic:
    print(dic[k],end=' ')