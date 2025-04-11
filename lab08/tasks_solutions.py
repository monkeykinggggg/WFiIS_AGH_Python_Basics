task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

def f1(filename,n):
    with open(filename) as f:
        lines = f.readlines()
        print(f'Pierwsze n linii: {lines[:n]}')
        print(f'Ostatnie n linii: {lines[-n:]}')
        print(f'Co n: {lines[::n]}')
        print(f'n-te slowo w kazdej linii: {[line.split(' ')[n] for line in lines]}')
        print(f'n-ty znak z kazej linii: {[line[n] for line in lines]}')
 
f1('zad1.in',2)

########### ZAD 2 ############
print()
task_index += 1
space = '#'*10
print(space+zadanie(task_index)+space)

folder_name = 'data'
file_regex = 'data*in'

import glob, os
import numpy as np

lists_from_files = []
for filename in glob.glob(os.path.join(folder_name, file_regex)):
    file_list = []
    with open(filename) as f:
        #print(f)
        lists_from_files.append([float(line.strip()) for line in f.readlines()])

with open('data.out','w') as f:
    f.write(f'Nr   Srednia Odchylenie\n')
    i=0
    for tup in  zip(*lists_from_files):
        i+=1
        f.write(f'{i:>2}{np.average(tup):>10.3f}{np.std(tup):>11.3f}\n')

        
########### ZAD 3 ############
print()
task_index += 1
space = '#'*10
print(space+zadanie(task_index)+space)

def create_file_for_plotting(filename):
    with open(filename,'w') as f:
        f.write('''
import matplotlib.pyplot as plt
import numpy as np
from glob import glob

plt.xlabel('Nr wiersza')
plt.ylabel('Wartości')

for file in glob('data/data*in'):
    with open(file) as f:
        ys = [float(line.strip()) for line in f.readlines()]
        plt.scatter(np.linspace(1,len(ys),len(ys)),ys,label=file)
with open('data.out') as f:
    lines = f.readlines()
    avgs = [float(line.split()[1]) for line in lines[1:]]
    stds = [float(line.split()[2]) for line in lines[1:]]
    plt.errorbar(np.linspace(1,len(avgs),len(avgs)),avgs,marker='*',yerr=stds,label = 'data.out')
plt.legend()
plt.savefig('zad3.png')
                ''')
        
create_file_for_plotting('zad3_plotting.py')


########### ZAD 4 ############
print()
task_index += 1
space = '#'*10
print(space+zadanie(task_index)+space)

glob_dict = {}
folder_name = 'rank'
for filename in glob.glob(os.path.join(folder_name,'*txt')):
    with open(filename) as f:
        #print(f)
        year = int(f.name.split('/')[1].split('.')[0])
        lines = [line.split() for line in f.readlines() ]           # list[list:imie,ranking]
        for name, rank in lines:
            #print(name,rank)
            glob_dict.setdefault(name,{}).setdefault(year,rank)
        
with open('rank.out','w') as f:
    f.write(f'Nazwisko')
    for rok in range(21):
        f.write(f'{2000+rok:>5}')
    for imie,tablica_wynikow in glob_dict.items():
        f.write(f'\n{imie:10}')
        wyniki = dict(sorted([(rok, rank) for rok,rank in tablica_wynikow.items()]))
        for rocznik in range(2000, 2021):
            if rocznik in wyniki:
                f.write(f'{wyniki[rocznik]:5}')
            else:
                f.write(f'{'-':5}')
        
        
########### ZAD 5 ############
print()
task_index += 1
space = '#'*10
print(space+zadanie(task_index)+space)

all_words = []
for filename in glob.glob('zad5*in'):
    with open(filename) as f:
        words_from_file = []
        for line in f.readlines():
            words_from_file.extend(line.split())
        all_words.extend(words_from_file)
        
all_words = [word.lower() for word in all_words]
dictionary_of_letters={}
for word in all_words:
    if word[0].isalpha():
        dictionary_of_letters.setdefault(word[0],[]).append(1)
        
dictionary_of_letters = {letter:len(lst) for letter,lst in dictionary_of_letters.items()}
histogram = dict(sorted([(k,v) for k,v in dictionary_of_letters.items()],key = lambda x: x[1]))

print(f'Histogram posortowany po liczbie slow na dana litere\n: {histogram}')
# utworzenie wykresu histogramu w pliku: zad5_plotting.py
