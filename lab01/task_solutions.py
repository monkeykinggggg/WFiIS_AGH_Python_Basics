########### ZAD 1 ############
i=1
def zadanie(i):
    return f' ZAD {i} '

space = '#'*10
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
val_to_find = 10
print(f'{k=}')
for index in range(len(k)-1,-1,-1):
    if k[index] == val_to_find:
        print(f"Znaleziono {val_to_find} na pozycji {index}")
        del k[index]
        
print(f'{k=}')
try:
    k.index(val_to_find)
except ValueError:
    print(f'Nie znaleziono {val_to_find} w liście')
    
########### ZAD 2 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12]
print(f'{k=}')

while k.count(val_to_find)>0:
    print(f'Znaleziono {val_to_find} na pozycji {k.index(val_to_find)}')
    k.remove(val_to_find)
print(f'{k=}')

# UWAGA! mozna szybciej:
while val_to_find in k:
    print(f'Zneleziono {val_to_find} na pozycji: {k.index(val_to_find)}')
    k.remove(val_to_find)
    
########### ZAD 3 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(f'{k=}')
for index in range(1,len(k),2):
    print(k[index], end=' ')
print()
    
########### ZAD 4 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(k[1::2])                                  #! UWAGA: Zadanie na list slices

########### ZAD 5 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(f'{k=}')
for index in range(len(k)-1,-1,-2):
    print(k[index], end=' ')
print()

########### ZAD 6 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
print(k[len(k)-1::-2])                          #! Nie potrzebujemy drugiego argumentu do list slice   

########### ZAD 7 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
nowa = [(i,v) for i,v in enumerate(k)]
print(nowa)

########### ZAD 8 ############
i+=1
print()
print(space+zadanie(i)+space)

nowa.sort(key = lambda krotka: krotka[1])
print(nowa)

########### ZAD 9 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
nowa_parzysta = [(i,v) for i,v in enumerate(k) if v%2 == 0]
print(nowa_parzysta)

########### ZAD 10 ############
i+=1
print()
print(space+zadanie(i)+space)

k=[8,0,17,1,10,13,19,13,10,3,11,12,]
nowa_mniejszy_wiekszy = [(i,v) if i<v else (v,i) for i,v in enumerate(k)]               #! Very nice usage of ifs inside for loop in list comprehension
print(nowa_mniejszy_wiekszy)

########### ZAD 11 ############
i+=1
print()
print(space+zadanie(i)+space)

def print_2D_list(lista_2D,dim):
    print(f'lista_2D:')
    for i in range(dim):
        for j in range(dim):
            print(lista_2D[i][j],end = ' ')
        print()

dim = 9
square_dim = 5
# zeby ładnie bbyło wyśrodkowane, to oba wymiary parzyste albo oba nieparzyste
lista1 = [[1 if i>=(dim-square_dim)/2 and i<square_dim+(dim-square_dim)/2 and j>=(dim-square_dim)/2 and j<square_dim+(dim-square_dim)/2 else 0 for j in range(dim)] for i in range(dim)]
print_2D_list(lista1,dim)


lista2 = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]
print_2D_list(lista2,dim)

lista3 = [[1 if i==dim-1-j else 0 for j in range(dim)] for i in range(dim)]
print_2D_list(lista3,dim)

lista4 = [[1 if i==dim-1-j or i==j else 0 for j in range(dim)] for i in range(dim)]
print_2D_list(lista4,dim)

lista5 = [[1 if i%2 != j%2 else 0 for j in range(dim)] for i in range(dim)]
print_2D_list(lista5,dim)