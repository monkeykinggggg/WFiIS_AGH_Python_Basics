task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

def gen1():
    n = 1
    while True:
        yield n
        n+=1
    
def gen2(seq):
    
    def doskonala(liczba):
        if isinstance(liczba,int) and liczba > 0:
            suma = sum([kandydat for kandydat in range(1,liczba) if liczba%kandydat==0])
            if suma == liczba:
                return True
        return False

    yield from filter(doskonala,seq)
        
def gen3(seq, limit):
    for el in seq:
        if el>limit:
            return
        yield el
                
liczby_naturalne = gen1()
for _ in range(20):
    print(next(liczby_naturalne),end=', ')
    
print('\nLiczby doskonale: ',end=' ')
for i in gen2(range(10000)):
    print(i,end=', ')
    
print()

for el in gen3(range(100),11):
    print(el, end=' ')

########### ZAD 2 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)

from math import log
def gen4(u0 = 0, x0 = 1, a = 0.05):
    ui, xi = u0, x0 - a
    i=1
    while xi <= 1.5:
        xi = xi + a
        ui = ui + a/xi
        yield(xi,ui,log(xi))
        i += 1
    
for el in gen4():
    print(el)
    
########### ZAD 3 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)

from math import factorial,sin,fabs

def gen5(x):
    my_sin = 0
    k=0
    while True:
        my_sin += (-1)**k/factorial(1+2*k)*x**(1+2*k)
        yield (f'Wyraz ciagu: {k+1}, przyblizenie oraz sin dokladny: {my_sin}\t{sin(x)}')
        k+=1
        
        if fabs(my_sin-sin(x)) < 1e-8:
            return
        
for el in gen5(1):
    print(el)
    
########### ZAD 4 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)

from math import ceil

def gen6(*params):
    if len(params) == 1:
        stop = params[0]
        start = 0
        step = 1
    elif len(params) == 2:
        start, stop = params
        step = 1 
    elif len(params) == 3:
        start, stop, step = params
        
    else:
        print('Niepoprawne parametry')
        
    for i in range(ceil((stop-start)/step)):
        yield start 
        start += step

sekwencje_do_testowania = [range(10), range(-10), range(1,10), range(10,1), range(1,10,2), range(1,10,-2), range(10,1,2), range(10,1,-2)]
testy_generatorowe = [gen6(10), gen6(-10), gen6(1,10), gen6(10,1), gen6(1,10,2), gen6(1,10,-2), gen6(10,1,2), gen6(10,1,-2)]

for ran, gen in zip(sekwencje_do_testowania, testy_generatorowe):
    print('range: ')
    for el in ran:
        print(el,end=' ')
    print()
    print('Sprawdzenie: ')
    for el in gen:
        print(el,end=' ')
    print()


########### ZAD 5 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)

from random import uniform, choice

def gen6(start = 1.0):
    curr = start
    while True:
        przedzial = uniform(0.4,1.0)
        kierunek = choice([-1,1])
        curr = curr + kierunek*przedzial
        if curr < 0.1:
            return 
        yield curr
        

for number in gen6():
    print(f'{number:.2f}')