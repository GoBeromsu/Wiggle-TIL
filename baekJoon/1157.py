import sys

input = sys.stdin.readline().rstrip().upper()

dic = {}

for i in range(len(input)):
    val = input[i]
    if (val in dic):
        count = {val :(dic[val] +1)}
        dic.update(count)
    else:
        dic[val] = 1

sorted_dict = sorted(dic.items(), key = lambda item: item[1],reverse=True)
maxVal = sorted_dict[0][1]
maxKey = sorted_dict[0][0]
for key,value in sorted_dict:
    if(maxVal<value):
        maxVal=value
        maxKey=key
    elif(maxVal==value and maxKey!=key):
        maxKey="?"
        break

print(maxKey)