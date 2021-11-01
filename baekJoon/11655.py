import sys

def calcPos(num):
    if num +13 >26:
        return num -13
    else:
        return num + 13

for s in sys.stdin.readline().rstrip():
    askii = ord(s)
    if 65<=askii and askii  <91:
        print(chr(64+calcPos(askii-64)),end='')
    elif 97<=askii and askii <123:
        print(chr(96+calcPos(askii-96)),end='')
    else:
        print(s,end='')