from itertools import permutations

def Permutations(s):
    p=permutations(s)
    for i in list(p):
        print(''.join(i))
Permutations('ABCe')        
 