import sys

stack = []
num = int(sys.stdin.readline())
exp = list(sys.stdin.readline().rstrip())

dic = {chr(key+65):int(sys.stdin.readline()) for key in range(num)}

for s in exp:
    if s.isalpha():
        stack.append(dic[s])
    else:
        n1=stack.pop()
        n2=stack.pop()
        if s=='+':
            stack.append(n1+n2)
        elif s=='-':
            stack.append(n2-n1)
        elif s=='*':
            stack.append(n2*n1)
        elif s=='/':
            stack.append(n2/n1)

print(F"{stack[0]:.2f}")