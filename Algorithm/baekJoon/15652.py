import sys


def dfs(result: list, n: int, m: int):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in range(1, n + 1):
        if not result:
            result.append(i)
            dfs(result, n, m)
            result.pop()
        else:
            if result[-1] <= i:
                result.append(i)
                dfs(result, n, m)
                result.pop()


n, m = map(int, sys.stdin.readline().split())
result = []
dfs(result, n, m)
