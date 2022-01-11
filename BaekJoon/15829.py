import sys

input=int(sys.stdin.readline())
inString = sys.stdin.readline().rstrip()
sum=0
dic={}

for i in range(1,27):
    dic[chr(i+96)]=i

for i in range(input):
    sum+=(dic[inString[i]]* pow(31,i))

print(sum%1234567891)