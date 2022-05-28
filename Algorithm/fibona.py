import sys

dic = {0: 1, 1: 1}


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 2) + fibo(x - 1)


def fibo_memoization(x):
    if x in dic:
        return x
    else:
        dic[x] = fibo_memoization(x - 2) + fibo_memoization(x - 1)
        return dic[x]

print(f"memoization o : {fibo_memoization(100)}")
print("계산 중이라 오래 걸리는거임")
print(f"memoization x : {fibo(100)}")
