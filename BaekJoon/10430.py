getInput = input().split()

a=int(getInput[0])
b=int(getInput[1])
c=int(getInput[2])

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)