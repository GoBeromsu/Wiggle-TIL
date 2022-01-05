import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
result = []


def dfs(n, m, numbers, result):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for num in numbers:
        if result:
            if result[-1] < num:
                result.append(num)
                dfs(n, m, numbers, result)
                result.pop()
        else:
            result.append(num)
            dfs(n, m, numbers, result)
            result.pop()

dfs(n, m, numbers, result)
