import random
import numpy as np

def queenprint(solution):
    def line(pos,length=len(solution)):
        return '. '*(pos)+'♕ '+'. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

#Рекурсивное решение

def conflict(state,col):
    row=len(state)
    for i in range(row):
        if abs (state [i] - col) in (0, row-i): 
            return True
    return False
    
def recuersive_resolve(num=8,state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state)==num-1:
                yield(pos,)
            else:
                for result in recuersive_resolve(num, state+(pos,)):
                    yield (pos,)+result
            

queenprint(random.choice(list(recuersive_resolve())))

print('')

#Итеративное решение
 
def under_attack(col, queen):
    return col in queen or any(abs(col - x) == len(queen) - i for i, x in enumerate(queen))
 
 
def solve(size):
    solutions = [[]]
    row = 0
    while row < size:
        solutions = [solution + [i + 1]
                     for solution in solutions
                     for i in range(size)
                     if not under_attack(i + 1, solution)]
        row+=1

    return solutions
 
def iterative_resolve(size):
    result = np.array(solve(size))
    for i in result:
        np.sort(i)
    for num in range(8):
        result[1][num]-=1
        
    queenprint(tuple(result[1]))
     
iterative_resolve(8)