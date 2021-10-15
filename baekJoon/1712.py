
import math

inputs= input().split()

fixedPrice= int(inputs[0])
makingPrice = int(inputs[1])
sellingPrice = int(inputs[2])

if(sellingPrice<=makingPrice):
    print(-1)
else:
    print(int((fixedPrice/(sellingPrice-makingPrice)+1)))