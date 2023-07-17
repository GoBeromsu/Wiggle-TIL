import sys

sentence = sys.stdin.readline().rstrip()

arr =[]
for s in range(len(sentence)):
    arr.append(sentence[s::])

for s in sorted(arr):
    print(s)