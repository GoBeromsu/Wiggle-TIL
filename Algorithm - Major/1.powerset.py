data = ['a','b','c','d','e','f']
n = len(data)
include = [ False for _ in range(n)]

def powerset(k:int):
    if k==n:
        for i in range(n):
            if include[i]:
                print(data[i],end=' ')
        print()
    else:            
        include[k]= False
        powerset(k+1)
        include[k] = True
        powerset(k+1)
powerset(0)