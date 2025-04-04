i=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(i)+space)

import sys
print(f'{sys.argv[1:]=}')

if len(sys.argv)==1:
    print('Nieprawidłowe wywołanie programu. Potrzebujemy przynajmniej jednego parametru')
else:
    napis = ' '.join(sys.argv[1:])
    print(f'String z elementów listy argv: {napis}')

########### ZAD 2 ############
print()
i+=1
space = '#'*10
print(space+zadanie(i)+space)

import string
male_litery = [el for el in napis if el in string.ascii_lowercase]
duze_litery = [el for el in napis if el in string.ascii_uppercase]
#!mozna bylo duzo prosciej bez modulu:
cyfry = [el for el in napis if el.isdigit()]
no_letters = [el for el in napis if not el.isalpha()]
print(f'{male_litery=}')
print(f'{duze_litery=}')
print(f'{cyfry=}')
print(f'{no_letters=}')

########### ZAD 3 ############
print()
i+=1
space = '#'*10
print(space+zadanie(i)+space)

male_litery_bez_powtorzen = [el for idx,el in enumerate(male_litery) if el not in male_litery[:idx]]
print(f'Lista bez powtorzen: {male_litery_bez_powtorzen}')

krotnosc_liter = [(el,male_litery.count(el)) for el in male_litery_bez_powtorzen]
print(f'Lista z krotkami: {krotnosc_liter}')

########### ZAD 4 ############
print()
i+=1
space = '#'*10
print(space+zadanie(i)+space)

print(sorted(krotnosc_liter, key = lambda krotka:krotka[1], reverse=True))

########### ZAD 5 ############
print()
i+=1
space = '#'*10
print(space+zadanie(i)+space)

napis = ' '.join(sys.argv[1:])
a = 0
for samogloska in 'aeiouy':
    a += napis.lower().count(samogloska)
b = 0    
for litera in string.ascii_letters:
    b += napis.lower().count(litera)

b -= a

funkcja_liniowa_krotki = [(int(x),a*int(x)+b) for x in cyfry]               # type(x) = str
print(funkcja_liniowa_krotki)

########### ZAD 6 ############
i+=1
print()
space = '#'*10
print(space+zadanie(i)+space)

average_x = sum(int(x) for x in cyfry)/len(cyfry)
d = sum(float(x)-average_x for x in cyfry)/len(cyfry)
a=0
try:
    a = sum(y*(x-average_x) for x,y in funkcja_liniowa_krotki)/d
except ZeroDivisionError:
    print('Dzielenie przez zero, zmien dane')
    
average_y = sum(y for x,y in funkcja_liniowa_krotki)/len(funkcja_liniowa_krotki)
b = average_y-a*average_x

print(f'Wspolczynniki: {a=} {b=}')
