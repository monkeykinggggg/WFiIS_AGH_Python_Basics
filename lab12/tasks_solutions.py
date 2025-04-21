task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import abc
import math

class Calka(abc.ABC):
    def __init__(self,start,stop,n,func):
        if not isinstance(start, (float,int)) or not isinstance(stop, (float,int)) or start>stop:
            raise ValueError('Granica calkowania powinna byc liczbą, pierwsza powinna być mniejsza od drugiej')
        if not isinstance(n, int) or n<=0:
            raise ValueError('n powinno byc dodatnim int-em')
        if not callable(func):
            raise ValueError('ostatnim argumentem powinna być referencja do funkcji')
        self.xp = start
        self.xk = stop
        self.n = n
        self.func = func
        
    @abc.abstractmethod
    def evaluate(self):
        '''Oblicza numerycznie wartość całki z funkcji (func) od (xp) do (xk) w (n) krokach'''
        
class Simpson(Calka):
    def __init__(self,start,stop,n,func):
        super().__init__(start, stop, n, func)
        
    def evaluate(self):
        '''Metoda Simsposona do wyliczania wartosci calki'''
        h = (self.xk-self.xp)/(self.n*2)
        sum1 = sum(self.func(self.xp + i*h) for i in range(1,2*self.n,2))
        sum2 = sum(self.func(self.xp + i*h) for i in range(2,2*self.n,2))
        s = h/3 * ( self.func(self.xp)+ 4*sum1 + 2*sum2 + self.func(self.xk) )
        return s
    
class Trapez(Calka):
    def __init__(self,start,stop,n,func ):
        super().__init__(start,stop,n,func)
        
    def evaluate(self):
        '''Metoda Trapwzow do wyliczania wartosci calki'''
        h = (self.xk-self.xp)/(self.n)
        sum1 = sum(self.func(self.xp+h*i) + self.func(self.xp+h*(i+1)) for i in range(1,self.n))
        return h/2*sum1
    

f = lambda x: math.log(x**3 + 3*x**2 + x + 0.1) * math.sin(18 * x)
xp,xk = 0,1
n = 1000
print(f'Całka wyliczona metodą Simpsona: ')
print(Simpson(xp,xk,n,f).evaluate())
print(f'Całka wyliczona metodą Trapezów: ')
print(Trapez(xp,xk,n,f).evaluate())


########### ZAD 2 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)


import copy 
import random

class Stos:
    def __init__(self, *iterable):
        self.items = []
        if iterable:
            self.items.extend(iterable)
            
            
    def __add__(self,value):
        ''' Metoda pozwalająca dodać jeden obiekt do stosu lub pełen obiekt typu Stos '''
        if isinstance(value,Stos):
            self.items.extend(value.items)
            return self
        else:
            self.items.append(value)
        
    def pop(self, index = -1):
        ''' Metoda usuwa element o określonym indeksie albo domyślnie ostatni '''
        del self.items[index]
        
    def length(self):
        ''' Metoda zwracająca długość stosu '''
        return len(self.items)
        
    def __str__(self):
        '''Funkcja zwracająca reprezentację stosu'''
        return str(self.items)
  
help(Stos) 
print('Testy klasy Stos: ')      
s1 = Stos(10)
s2 = Stos(20,30,40)
print(s1)
s1+20
print(s1)
s1+s2
print(s1)

class SortedStos(Stos):
    def __init__(self, *iterable, reverse = False):
        super().__init__(*iterable)
        self.reverse = reverse
        self.items.sort(reverse = self.reverse)
        
        
    def push(self, val):
        ''' Metoda do dodawania pojedynczej wartosci do testów w zadaniu.
            Dodaje tylko pod warunkiem że wartośc pasuje'''
        if not self.items:
            self.items.append(val)
        else:
            if (self.reverse and val<self.items[-1]) or (not self.reverse and val>self.items[-1]):
                self.items.append(val) 

        
    def __add__(self,value):
        ''' Metoda pozwalająca dodać jeden obiekt do stosu lub pełen obiekt typu Stos.
            W przypadku dodawania elementu typu Stos, musimy zachować porządek sortowania.'''
        if isinstance(value,SortedStos):
            if not self.reverse and not value.reverse:
                if self.items[0]>=value.items[-1]:
                    tmp = self.items
                    self.items = copy.deepcopy(value.items) 
                    self.items.extend(tmp)
                    return self
                elif self.items[-1]<=value.items[0]:
                    self.items.extend(value.items)
                    return self
                else:
                    raise ValueError('Stosy do siebie nie pasuja')
            elif self.reverse and value.reverse:
                if self.items[-1]>=value.items[0]:
                    self.items.extend(value.items)
                    return self
                elif self.items[0]<=value.items[-1]:
                    tmp = self.items
                    self.items = copy.deepcopy(value.items)
                    self.items.extend(tmp)
                    return self
                else:
                    raise ValueError('Stosy do siebie nie pasuja')
            else:
                raise ValueError('Stosu nie mozna dodać ze względu na inny rodzaj sortowania')                     
        elif isinstance(value,(int,float)):
            if self.reverse:
                for i,v in enumerate(self.items):
                    if v<=value:
                        self.items.insert(i,value)
            else:
                for i,v in enumerate(self.items):
                    if v>=value:
                        self.items.insert(i,value)
        else:
            raise ValueError('Nieprawidłowy typ danych do dodania. Może być typ numeryczny lub obiekt typu SortedStos')
        
        
print('Test Posortowanego Stosu: ')
ss1 = SortedStos(1,7,9,2,5)
ss2 = SortedStos(5,6,8,8,0,reverse=True)
print(ss1)
print(ss2)
try:
    ss1+ss2
except Exception as exc:
    print(exc)

ss3 = SortedStos(0,0,1)
print(ss1+ss3)


mean_length = 0
for i in range(100):
    ss = SortedStos()
    for _ in range(100):
        ss.push(random.randint(0,100))
    mean_length+=ss.length()

mean_length/=100
print(f'Średni rozmiar stosu rosnącego: {mean_length}')

########### ZAD 3 ############
print()
task_index+=1
space = '#'*10
print(space+zadanie(task_index)+space)

class MyClass:
    lines_from_files = []
    words_from_files = []
    chars_from_files = []
    filenames = []
    
    def __init__(self, filename):
        self.filename = filename
        self.count_elements()
        MyClass.lines_from_files.append(self.lines)
        MyClass.words_from_files.append(self.words)
        MyClass.chars_from_files.append(self.chars)
        MyClass.filenames.append(filename)
        
    def count_elements(self):
        with open(self.filename) as f:
            lines = f.readlines()
            self.lines = len(lines)
            words_in_lines = [line.split() for line in lines]
            self.words = sum(len(words_arr) for words_arr in words_in_lines)
            self.chars = sum(sum(len(word) for word in line_words) for line_words in words_in_lines)
        
    @staticmethod
    def wc_log():
        for i in range(len(MyClass.lines_from_files)):
            print(f'{MyClass.lines_from_files[i]:4} {MyClass.words_from_files[i]:4} {MyClass.chars_from_files[i]:4} {MyClass.filenames[i]}')
        print(f'{sum(MyClass.lines_from_files):4} {sum(MyClass.words_from_files):4} {sum(MyClass.chars_from_files):4} razem')
        
ob1 = MyClass('../lab10/tasks_solutions.py')
ob2 = MyClass('../lab09/tasks_solutions.py')
ob3 = MyClass('../lab08/tasks_solutions.py')
MyClass.wc_log()
        