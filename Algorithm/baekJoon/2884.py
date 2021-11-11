value=input().split()
hour = int(value[0])
minute = int(value[1])

if(minute-45<0):
    minute = (15+minute)
    if (hour>0):
        hour = hour - 1
    else:
        hour = 23 
else:
    minute = minute -45

print("{} {}".format(hour,minute))