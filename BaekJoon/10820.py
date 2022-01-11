import sys

def fun(s):
    
    small,big,number,space=0,0,0,0

    for val in s:
        if val.isupper():
            big+=1
        elif val.islower():
            small+=1
        elif val == ' ':
            space+=1
        elif val.isdigit():
            number+=1
        else:
            return -1
            break
    return f"{small} {big} {number} {space}"

while 1:
    try:
        s = sys.stdin.readline().rstrip('\n')
        print(len(s))
        if not s:
            break
        else:
            ans = fun(s)
            if ans ==-1:
                break
            else:
                print(ans)

    except EOFError:
        break