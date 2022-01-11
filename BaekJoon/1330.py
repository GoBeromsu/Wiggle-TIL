temp = input().split()

a= int(temp[0])
b= int(temp[1])

if (a<b):
    print("<")
elif (a>b):
    print(">")
else:
    print("==")