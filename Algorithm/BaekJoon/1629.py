import sys

MAX = 2147483647
a,b,c = map(int,sys.stdin.readline().split())

print((a**b)%c)