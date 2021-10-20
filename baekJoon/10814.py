import sys

num = int(sys.stdin.readline())
dic={}
for i in range(num):
    input=sys.stdin.readline().split()
    key = int(input[0])
    value= input[1]
    arr= []
    if key in dic:
        arr = dic[key]
        arr.append(value)
        dic[key] = arr
    else:
        dic[key] = [value]
    
for key, value in sorted(dic.items()):
    for i in range(len(value)):
        print(f"{key} {value[i]}")