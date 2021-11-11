import sys

inputs = []
while True:
    input = list(map(int, sys.stdin.readline().split()))
    if input[0] == 0 and input[1] == 0 and input[2] == 0:
        break
    inputs.append(input)

for input in inputs:
    input = sorted(input)
    triangle = pow(input[1], 2) + pow(input[0], 2)

    if pow(input[2], 2) == triangle:
        print("right")
    else:
        print("wrong")
