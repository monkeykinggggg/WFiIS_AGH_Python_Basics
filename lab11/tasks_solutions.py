task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)


class ArithmeticSeries1:
    def __init__(self,pocz = 1,constant = 1,its = 10):
        self.pocz = pocz
        self.constant = constant
        self.iterations = its

    def __iter__(self):
        return self
    
    def __next__(self):
        tmp = self.pocz
        self.pocz += self.constant
        self.iterations -= 1
        if self.iterations >= 0:
            return tmp
        else:
            raise StopIteration

class ArithmeticSeries2:
    def __init__(self,pocz = 1,constant = 1,its = 10):
        self.pocz = pocz
        self.constant = constant
        self.iterations = its

    def __iter__(self):
        return ArithmeticSeries2(self.pocz,self.constant,self.iterations)
    
    def __next__(self):
        tmp = self.pocz
        self.pocz += self.constant
        self.iterations -= 1
        if self.iterations >= 0:
            return tmp
        else:
            raise StopIteration
        
print('Pierwszy sposob:')
as1 = ArithmeticSeries1(pocz = 24,constant=-4)
for el in as1:
    for elz in as1:
        print(f'{el:3},{elz:3}',end = ';')
    print()
print()

print('Drugi sposob:')
as2 = ArithmeticSeries2(pocz = 24, constant=-4)
for el in as2:
    for elz in as2:
        print(f'{el:3},{elz:3}',end = ';')
    print()
print()


########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import math

class RandomIterator:
    m = 2**48
    a = 44485709377909
    c = 0
    
    def __init__(self,x0 = 1):
        self.x = x0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.x = (self.a*self.x+self.c)%self.m
        return self.x / (self.m-1)
    
ri = RandomIterator()
print(f'Random iterator first 20 elements:')
for i in range(20):
    print(next(ri))
print()

f = lambda x: math.sin(x)
xmin, xmax = 0, math.pi
ymin, ymax = -10, 10
expected_value = 2
eps = 10**-3

n, t = 0, 0
while True:
    n += 1
    x = next(ri) * (xmax - xmin) + xmin
    y = next(ri) * (ymax - ymin) + ymin
    if y > 0 and y <= f(x):
        t += 1
    if y < 0 and y >= f(x):
        t -= 1
    integral = (xmax - xmin) * (ymax - ymin) * t / n
    #print(integral)
    if abs(integral - expected_value) < eps:
        break
print(f'Wyliczono całkę po {n} iteracjach. Wynik: {integral}')

########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import numpy as np

def numerical_derivative(f, x, dx=1e-6):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

class msceZerowe():
    def __init__(self, func, x0, eps = 10** -3):
        self.x = x0
        self.func = func
        self.eps = eps
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if abs(self.func(self.x)) < self.eps:
            raise StopIteration
        self.x = self.x - self.func(self.x)/numerical_derivative(self.func,self.x)
        return self.x
    
    
it2 = msceZerowe(lambda x: np.sin(x)-0.5*x, 1.5, eps = 10**-5)
for el in it2:
    print(el)
