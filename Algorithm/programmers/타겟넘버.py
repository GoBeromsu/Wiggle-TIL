from collections import deque
def solution(numbers, target):
    answer = 0
    numbers = deque(numbers)
    result = deque()
    while numbers:
        n = numbers.popleft()
        temp = deque()
        if len(result)==0:
            result.append(n)
            result.append(-n)
        else:
            for r in result:
                temp.append(r+n)
                temp.append(r-n)
            result = temp
            print(result)
    for r in result:
        if r==target:
            answer+=1
    return answer


print(solution([1,1,1,1,1],3))