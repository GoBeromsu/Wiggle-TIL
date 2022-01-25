import sys

# 부등호의 갯수
# k = int(sys.stdin.readline())
# sign = list(sys.stdin.readline().split())
k = 2
sign = ['<','>']

numbers = [0,1,2,3,4,5,6,7,8,9]
mxm,mim = 0,0
# 선택된 숫자는 모두 달라야함
# 부등호에 올 수 있는 숫자는 0~9
# 부등호가 무조건 성립해야함
# 부등호를 빼면 숫자가 생김 -> 이 숫자들의 최대와 최소 구하라

def backtrack(sindex:int,result:list):
    # base case
    if sindex==k:
        mxm=min(mxm,makeInt(result) )
        mxm=max(mxm, makeInt(result))
    else:
        if checkSign(sindex):
            for n in numbers:
                if result[-1]>n:
                    backtrack(sindex+1, result+[n])
def checkSign(sindex:int):
    if sign[sindex] =='>':
        return True
    return False
def makeInt(result:list):
    result = list(map(str,result))
    number = ''.join(result)
    return int(number)

# print할 때 자릿수 체크해서 출력해야함 0 때문에