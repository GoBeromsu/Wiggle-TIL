import sys
import time

val = sys.stdin.readline().rstrip()
a = 97
arr=[-1 for i in range(26)]
dic ={}

for i in range(a,a+26):
    dic[chr(i)] = -1
# print(dic)
curr = time.time()
for i in range(len(val)):
    for j in range(a,a+26):
        if (val[i] == chr(j) and arr[j-a]==-1):
            arr[j-a]=i
for i in range(len(arr)):
    print(arr[i], end=' ')
last = time.time()
print()
print(f"List Time is {last-curr}")

curr2 = time.time()
for i in range(len(val)):
    for j in range(a,a+26):
        if val[i] == chr(j) and dic[chr(j)]==-1:
            dic[chr(j)] = i

for value in dic:
    print(dic[value], end=' ')
last2 = time.time()
print()
print(f"Dic Time is {last2-curr2}")
print(f"Dictionary가 {(last-curr)//(last2-curr2)}배 빠릅니다")