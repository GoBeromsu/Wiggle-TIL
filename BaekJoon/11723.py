import sys

n = int(sys.stdin.readline())
s = set()

def calc(command,factor):
    global s
    f = int(factor)
    if command =='add':
        s.add(f)
    elif command == 'remove':
        s = s.difference(set([f]))
        
    elif command == 'check':
        if f in s:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if f in s:
            s.remove(f)
        else:
            s.add(f)
    elif command == 'all':
        s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif command == 'empty':
        s= set([])
for i in range(n):
    commands = list(sys.stdin.readline().rstrip().split())
    if len(commands) == 2:
        command,factor = map(str,commands)
    else:
        command,factor = commands[0],0
    calc(command, factor)