import sys

num = int(sys.stdin.readline())
dic={}
for i in range(num):
    number = int(sys.stdin.readline())
    if number in dic:
        value = dic[number] +1
        dic[number] = value
    else:
        dic[number]=1

for number in sorted(dic.items()):
    count = number[1]
    for i in range(count):
        print(number[0])