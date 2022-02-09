import sys
from collections import deque
# queue의 가장 앞 문서의 중요도를 확인한다
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있으면 큐의 가장 뒤에 재배치
# 몇 번째로 인쇄되는지를 맞추는거지

# num = int(sys.stdin.readline())

# 문서를 출력하는 함수를 만들어서 테스트 케이스 받으면 출력하도록 하기


def que(length, target, importance):
    q = deque([0 for _ in range(length)])
    q[target] = 1
    count = 1
    t = target
    while 1:
        if importance[0] == max(importance):
            if q[0]==1 or length ==1:
                print(count)
                break
            importance.popleft()
            q.popleft()
            count += 1
        else:
            importance.append(importance.popleft())
            q.append(q.popleft())

num = int(sys.stdin.readline())
for i in range(num):
    length, target = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    que(length, target, deque(importance))
