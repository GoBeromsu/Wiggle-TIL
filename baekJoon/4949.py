import sys

# arr= [' ([(([])[]))] ']
def check(sentence):
    string = [char for char in sentence]
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s=='[':
            stack.append(s)
        if s == ')':
            if len(stack) == 0:
                return 'no'
            else:
                if stack[-1]=='[':
                    return 'no'
                else:
                    stack.pop()
        elif s== ']':
                if len(stack) == 0:
                    return 'no'
                else:
                    if stack[-1]=='(':
                        return 'no'
                    else:
                        stack.pop()  
    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'
arr = []
while 1:
    string = sys.stdin.readline().rstrip()
    if string =='.':
        break
    else:
        arr.append(string)

for sentence in arr:
    if '[' not in sentence and ']' not in sentence and '(' not in sentence and ')' not in sentence:
        print('yes')
        continue
    elif '[' in sentence and ']' not in sentence:
        print('no')
        continue
    elif '(' in sentence and ')' not in sentence:
        print('no')
        continue
    else:
        print(check(sentence))
    