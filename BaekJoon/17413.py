import sys

sentence = sys.stdin.readline().rstrip()
# sentence = '<int><max>2147483647<long long><max>9223372036854775807'
key =1 
stack = []
for s in sentence:
    if s == '<':
        key =-1
    if key ==-1:
        while stack:
            print(stack.pop(),end='')
        print(s,end='')
    else:
        if s ==' ':
            while stack:
                print(stack.pop(),end='')
            print(s,end='')
        else:
            stack.append(s)
    if s=='>':
        key =1
while stack:
    print(stack.pop(),end='')