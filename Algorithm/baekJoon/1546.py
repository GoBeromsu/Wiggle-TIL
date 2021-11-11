import sys

max=0
sum=0
num = int(sys.stdin.readline())
scores= list(map(int,sys.stdin.readline().split()))

max=scores[0]
for i in range(len(scores)):
    if (scores[i]>max):
        max=scores[i]

for i in range(len(scores)):
    sum +=scores[i]

print(float(sum/num/max*100))