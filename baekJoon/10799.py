import sys

sentence= list(sys.stdin.readline().rstrip())
sum =0
stack = []
for i in enumerate(sentence):
    if i[1] == '(':
        stack.append(i)
    else:
        if sentence[i[0]-1] == ')':
            stack.pop()
            sum+=1
        else:
            stack.pop()
            sum+=len(stack)
print(sum)