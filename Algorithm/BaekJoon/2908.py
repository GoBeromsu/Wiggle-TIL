import sys

input = list(map(str,sys.stdin.readline().split()))

val =[]

for i in range(2):
    val.append(int(input[i][2]+input[i][1]+input[i][0]))

if (val[0]>val[1]):
    print(val[0])
else:
    print(val[1])