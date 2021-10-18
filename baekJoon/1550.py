import sys

sum=0
dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

for i in range(0,10):
    dic[str(i)] = i

val = str(sys.stdin.readline().rstrip())

for i in range(len(val)):
    sum+=dic[val[i]]*pow(16,len(val)-1-i)

print(sum)