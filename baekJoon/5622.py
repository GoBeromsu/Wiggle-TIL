import sys

tups = [(1,"",2),
(2,"A",3),(2,"B",3),(2,"C",3),
(3,"D",4),(3,"E",4),(3,"F",4),
(4,"G",5),(4,"H",5),(4,"I",5),
(5,"J",6),(5,"K",6),(5,"L",6),
(6,"N",7),(6,"M",7),(6,"O",7),
(7,"P",8),(7,"Q",8),(7,"R",8),(9,"S",8),
(8,"T",9),(8,"U",9),(8,"V",9),
(9,"W",10),(9,"X",10),(9,"Y",10),(9,"Z",10)]

input = sys.stdin.readline().rstrip()
sum =0
for i in range(len(input)):
    for tup in tups:
        if(input[i]==tup[1]):
            sum+=tup[2]
print(sum)