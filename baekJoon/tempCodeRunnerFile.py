for i in range(num):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    people = [floor,room]
    arr.append(people)
for j in range(num):
    print(destNum(arr[j][0],arr[j][1]))
