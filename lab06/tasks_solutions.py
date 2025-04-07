task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)


import time
import sys

powt=1000
N=10000

def forStatement():
    # dodawanie elementow
    lista = []
    for i in range(N):
        lista.append(i)
        
    # dodawanie elementow podniesionych do kwadratu
    # lista = []
    # for i in range(N):
    #     lista.append(i**2)
    
    # sumowanie elementów z wykorzystaniem pętli for
    # s = 0
    # for el in lista:
    #     s+=el
    # return s
    
    # sumowanie z wykorzystaniem funkcji sum
    s = sum(el for el in lista)
    return s

def listComprehension():
    # dodawanie elementow
    # return [i for i in range(N)]
    
    # dodawanie elementow podniesionych do kwadratu
    # return [i**2 for i in range(N)]
    
    # sumowanie elementów z wykorzystaniem pętli for
    # lista = [i for i in range(N)]
    # s = 0
    # for el in lista:
    #     s+=el
    # return s
    
    # sumowanie z wykorzystaniem funkcji sum
    s = sum(i for i in range(N))
    return s
    

def mapFunction():
    # dodawanie elementow
    # return map(lambda x: x,range(N))
    
    # dodawanie elementow podniesionych do kwadratu
    # return map(lambda x: x**2,range(N))
    
    # sumowanie elementów z wykorzystaniem pętli for
    lista = map(lambda x: x,range(N))
    # s = 0
    # for el in lista:
    #     s+=el
    # return s
    
    # sumowanie z wykorzystaniem funkcji sum
    s = sum(lista)
    return s
    

def generatorExpression():
    # dodawanie elementow
    # return (i for i in range(N))
    
    # dodawanie elementow podniesionych do kwadratu
    # return (i**2 for i in range(N))
    
    # sumowanie elementów z wykorzystaniem pętli for
    lista = (i for i in range(N))
    # s = 0
    # for el in lista:
    #     s+=el
    # return s
    s = sum(lista)
    return s
    
    

def tester(func):
    start_time = time.time_ns()
    for _ in range(powt):
        func()
    end_time = time.time_ns()
    return f'{(end_time-start_time)/1000:>15} us'

print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
    
# # Dodawanie elementu
# forStatement         =>        154601.0 us
# listComprehension    =>        121126.0 us
# mapFunction          =>           147.0 us
# generatorExpression  =>           147.0 us

# # Dodawanie elementu do kwadratu
# forStatement         =>        319759.0 us
# listComprehension    =>        291344.0 us
# mapFunction          =>           150.0 us
# generatorExpression  =>           148.0 us

# # Sumowanie elementow z wykorzystaniem pętli for
# forStatement         =>        286288.0 us
# listComprehension    =>        255700.0 us
# mapFunction          =>        400522.0 us
# generatorExpression  =>        263044.0 us

# # Sumowanie z wykorzystaniem funkcji sum
# forStatement         =>        296150.0 us
# listComprehension    =>        209130.0 us
# mapFunction          =>        292639.0 us
# generatorExpression  =>        214555.0 us


########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import random

def Monte_carlo(N):
    # pi*R^2/4R^2 -> pi = 4*proportion
    proportion = len(list(filter(lambda x: x[0]**2+x[1]**2<=1,((random.uniform(-1,1),random.uniform(-1,1)) for _ in range(N)))))/N
    return 4*proportion
    
print(f'Wyznaczona wartość PI = {Monte_carlo(10000)}')


########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import math

def f3(xs,ys):
    x_avg = sum(xs)/len(xs)
    y_avg = sum(ys)/len(ys)
    D = sum(map(lambda x : (x - x_avg)**2,xs))
    a = sum(map( lambda x,y : (x-x_avg)*y,xs,ys))/D
    b = y_avg - a * x_avg
    d_y = math.sqrt(sum(map(lambda x,y: (y-(a*x+b))**2,xs,ys))/(len(xs)-2))
    d_a = d_y/math.sqrt(D)
    d_b = d_y * math.sqrt(1/len(xs) + x_avg**2/D)
    return a,b,d_a,d_b

n = range(100)
a,b,da,db = f3(range(100),[6*i+10 for i in range(100)])
print(f'Współczynniki wynoszą {a=}, {b=}\tich niepewności to: {da=}, {db=}')


########### ZAD 4 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)
    
    
def myreduce(func,seq):
    first_component = seq[0]
    for el in seq[1:]:
        first_component = func(first_component,el)
    return first_component
    
print(myreduce(lambda x,y:x+y,[1,2,10,9]))
print(myreduce(lambda x,y:x*y,[5,2,5]))


########### ZAD 5 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('Max w wierszach:')
print(list(map(max,matrix)),end='\n')       #! wystarczy użyć max zamiast lambda - wsadzamy referencję do funkcji tak samo

print('Max w każdej kolumnie')
print(list(map(lambda row: max(row),list(zip(*matrix)))),end='\n')


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[9, 10], [11, 12]]

suma = [ [sum(el) for el in zip(*rows_i)] for rows_i in zip(A,B,C)]

print('Suma macierzy:')
for el in suma:
    print(el)
