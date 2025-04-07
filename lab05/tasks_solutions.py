task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import sys
import random
import string

def f1(s):
    literals = string.ascii_lowercase.replace('x','')
    trans_mapping = str.maketrans({l : str(random.randrange(10)) for l in literals})
    translated_string = s.translate(trans_mapping)
    print(f'Równanie: {translated_string}')
    lista_xy = [(x,eval(translated_string)) for x in [random.uniform(0,1) for _ in range(10)]]
    return lista_xy

if len(sys.argv)==1:
    print(f'Nieprawidłowe wywołanie pragramu. Należy podać argument wiersza poleceń.')
else:
    print(f1(sys.argv[1]))
    
########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

def f2(*params):
    d = {}
    for tup in params:
        for el in tup:
            d.setdefault(el,[]).append(1)
    return [k for k,v in d.items() if len(v)==len(params)]
    
print(f2([1,2,3], (1,3,5), [3,2,1]))


#! Rozwiązanie z for-else :

def f2_better(*params):
    wyniki = []
    if len(params)>1:
        for el in params[0]:
            for it in params[1:]:
                if el not in it:
                    break           # nie znależliśmt tej samej wartości w którymś z iterables
            else:
                wyniki.append(el)
    else:
        print(f'Funkcja musi przyjąć przynajmniej 2 argumenty iterowalne')
    return wyniki

print('Rozwiązanie odpowiednie: ')
print(f2_better([1,2,3], (1,3,5), [3,2]))
print(f2_better([1,2,3], (1,3,5), [3,2,1]))
                
########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

def f3(sek1,sek2,p = True):
    lista = []
    if(p):
        lista = [(sek1[i],sek2[i]) for i in range(min(len(sek1),len(sek2)))]
    else:
        lista = [(sek1[i] if i<len(sek1) else None,sek2[i] if i<len(sek2) else None) for i in range(max(len(sek1),len(sek2)))]
    return lista

print(f3([1,2,3], (1,9)))
print(f3([1,2,3,5,5], (1,9), p = False))
print(f3([1,2,], (1,9,10,10), p = False))

########### ZAD 4 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

def f4(n):
    result = [[1],[1,1]]
    for i in range(2,n):
        row = [1]
        for j in range(i-1):
            row.append(result[i-1][j]+result[i-1][j+1])
        row.append(1)
        result.append(row)
    return result
    

n=6
result=f4(n)
max_width = len(str(result[-1][len(result[-1]) // 2])) + 2  # Add space for padding

for row in result:
    spaces = (n - len(row)) * max_width // 2
    print(' ' * spaces, end='') 
    for el in row:
        print(f'{el:{max_width}}', end='')  
    print()

########### ZAD 5 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import random

def f5(liczba_calkowita, start,stop,sposob_poszukiwania = 'r'):
    i=0
    while True:
        i+=1
        x = random.randint(start,stop) if sposob_poszukiwania == 'r' else (stop-start)//2+start
        print(x)
        if x < liczba_calkowita:
            start = x
        elif x > liczba_calkowita:
            stop = x
        else:
            print(f'Znaleziono liczbę {x} po {i} iteracjach')
            break
        

f5(5,5,10)
f5(5,5,10,'l')
