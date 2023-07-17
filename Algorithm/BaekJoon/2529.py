import sys, math

# 부등호의 갯수
k = int(sys.stdin.readline())
sign = list(sys.stdin.readline().split())

checker = [False] * 10
mxm, mim = "",""

def backtrack(sindex: int, result: str):
    # base case
    global mxm, mim
    if sindex == k+1:
        if not len(mim):
            mim=result
        else:
            mxm=result
        return
    else:
        for i in range(10):
            if not checker[i]:
                if sindex == 0 or checkSign(result[-1],str(i),sign[sindex-1] ):
                    checker[i] = True
                    backtrack(sindex + 1, result +str(i))
                    checker[i] = False

def checkSign( i, j,sign):
    if sign == "<":
        return i < j
    if sign == ">":
        return i > j


backtrack(0, "")
print(mxm)
print(mim)
