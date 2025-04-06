task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

from random import randrange, shuffle, choices,randint
from collections import defaultdict
import string

k = 10
lista1 = [randrange(5*k) for _ in range(k)]
lista1_kopia = lista1.copy()
print(f'{lista1=}')
dict1 = defaultdict(int)

for i in range(100):
    shuffle(lista1) # przemieszanie w mscu
    for idx in range(len(lista1)):
        if lista1[idx] == lista1_kopia[idx]:    # wartosc pozostala w miejscu
            dict1[idx] += 1

dict1 = dict(sorted(dict1.items()))   
print(dict1)


########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

losowy_string='.'.join(choices(string.ascii_lowercase,k=10))
print(f'{losowy_string=}')

########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

lista3 = [randrange(20) for _ in range(100)]
dict3a = {}

for i,v in enumerate(lista3):
    dict3a.setdefault(v,[]).append(i)
    
print(f'{dict3a=}')
print()

dict3b = {}

for val in lista3:      # idziemy pokolei po nastepnych elementach
    nmbr_of_indexes = lista3.count(val)
    idx_left = 0
    while nmbr_of_indexes>0:
        idx = lista3.index(val,idx_left)
        idx_left=idx+1
        dict3b.setdefault(val,idx)
        nmbr_of_indexes-=1

print(f'{dict3a=}')
print()

#! Duzo lepszy sposob:

dict3b_lepszy = {}
for val in lista3:
    dict3b_lepszy.setdefault(val,[]).append(lista3.index(val, 0 if not dict3b_lepszy[val] else dict3b_lepszy[val][-1]+1))
    
print(f'{dict3b_lepszy=}')

########### ZAD 4 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

n = randint(3,6)
print(f'Dla n={n}')

i=0
for _ in range(1000):
    liczba_losowa = randint(10**(n-1),10**(n)-1)
    #print(liczba_losowa)
    if str(liczba_losowa) == str(liczba_losowa)[::-1]:
        i+=1
print(i)        

#! W jednej linijce zrobione
print('Lepszy sposob: ')
palindromy = {n:sum([1 for _ in range(1000) if str(liczba:=randint(10**(n-1),10**(n)-1)) == str(liczba)[::-1]]) for n in range(3,7)}
print(palindromy)

    
########### ZAD 5 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

slownik1,slownik2 = {n: randrange(1,100) for n in range(1,11)},{n: randrange(1,100) for n in range(1,11)}
slownik1,slownik2 = {v:k for k,v in slownik1.items()}, {v:k for k,v in slownik2.items()}        # nie przejmujemy się nadpisywanymi wartościami dla kluczy, jeżeli klucz się powtórzy
print(slownik1)
print(slownik2)

concatenate_slownik = {key:(val1,slownik2[key]) for key,val1 in slownik1.items() if key in slownik2}
print(concatenate_slownik)