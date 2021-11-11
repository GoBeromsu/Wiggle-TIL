import sys

stack = []
num = int(sys.stdin.readline())
expression = list(sys.stdin.readline().rstrip())
dic = {chr(n+64):int(sys.stdin.readline()) for n in range(1,num+1)}

def calc(n1,n2,exp):
    if str(type(n1))=="<class 'int'>" or str(type(n1))=="<class 'float'>":
        pass
    else:
        n1 = dic[n1]
    if str(type(n2))=="<class 'int'>" or str(type(n2))=="<class 'float'>" :
        pass
    else:
        n2 = dic[n2]
    if exp=='+':
        return n1+n2
    if exp=='-':
        return n1-n2
    if exp=='*':
        return n1*n2
    if exp=='/':
        return n1/n2

for s in expression:
    if s in dic:
        stack.append(s)
    else:
        n1=stack.pop()
        n2=stack.pop()
        stack.append(calc(n2,n1,s))
print(f"{stack[0]:.2f}")

# for s in enumerate(expression):
#     idx = s[0]
#     val = s[1]
#     if val not in dic:
#         stack.append(val)
#     else:
#         if expression[idx-1] in dic:
#             stack.append(calc(val,stack.pop(),stack.pop()))
#         else:
#             stack.append(val)
#     # print(f" {s[0]}  :{stack}:{s[1]}")
# print(f"{stack[0]:.2f}")

