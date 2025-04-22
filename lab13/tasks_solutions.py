task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)


def parametrized_decorator(a,b):
    def decorator(func):
        def wrapper(p1,p2):
            for i in (p1.x,p1.y,p2.x,p2.y):
                if not(a <= i <= b):        # bardzo fajny sposob na czytelne porównywanie !
                    raise ValueError(f'Należy wykonywać działania na punktach w zakresie: {a} - {b}')
            else:
                return func(p1,p2)         # only when loop not broken before
        return wrapper
    return decorator


class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
    
    @parametrized_decorator(0,5)
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(other.x+self.x, other.y+self.y)
        else:
            raise ValueError('Niepoprawny typ danych')
        
    @parametrized_decorator(0,5)
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x-other.x, self.y-other.y)
        else:
            raise ValueError('Niepoprawny typ danych')
        

p1 = Point(1,2)
p2 = Point(3,3)
p3 = Point(6,2)
print(p1, p2)
print(p1+p2)
print(p2+p1)
print(p2-p1)
print(p1-p2)
########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)


try:
    print(p1+p3)
except Exception as e:
    print(e)
    print(f'Uzyto punktów: {p1} {p3}')

########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import math

class Formulas:
    
    @staticmethod
    def distance(p1,p2):
        return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    
    @staticmethod
    def Heron(*points):
        if len(points)==3:
            a = Formulas.distance(points[0],points[1])
            b = Formulas.distance(points[1],points[2])
            c = Formulas.distance(points[0],points[2])
            obw = a+b+c
            p = obw/2
            P = math.sqrt(p*(p-a)*(p-b)*(p-c))
            return obw, P
        else:
            raise ValueError(f'Nieprawidłowa liczba punktów do metody Herona. Podano: {len(points)}')
        
    @staticmethod
    def Brahmagupta(*points):
        if len(points)==4:
            a = Formulas.distance(points[0],points[1])
            b = Formulas.distance(points[1],points[2])
            c = Formulas.distance(points[2],points[3])
            d = Formulas.distance(points[3],points[0])
            obw = a+b+c+d
            p = obw/2
            P = math.sqrt(p*(p-a)*(p-b)*(p-c)*(p-d))
            return obw, P
        else:
            raise ValueError(f'Nieprawidłowa liczba punktów do metody Brahmagupty. Podano: {len(points)}')
        
testing_points = [Point(x,y) for y in [0,1] for x in [0,1]]
try:
    obw1, p1 = Formulas.Heron(*testing_points[:-1])
    print(f'Obwód wynosi: {obw1}, pole: {p1}')
    obw2, p2 = Formulas.Heron(*testing_points)
    print(f'Obwód wynosi: {obw2}, pole: {p2}')
except Exception as e:
    print(e)
    
try:
    obw2, p2 = Formulas.Brahmagupta(*testing_points)
    print(f'Obwód wynosi: {obw2}, pole: {p2}')
    obw1, p1 = Formulas.Brahmagupta(*testing_points[:-1])
    print(f'Obwód wynosi: {obw1}, pole: {p1}')
except Exception as e:
    print(e)
    
########### ZAD 4 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)


class Funktor:
    functionCallCounter = {}
    
    def __init__(self, func):
        self.func = func
        Funktor.functionCallCounter[func.__name__] = 0      # adding key to dict
    
    def __call__(self, *args, **kwargs):
        Funktor.functionCallCounter[self.func.__name__] +=1
        return self.func(*args, **kwargs)
    
    @staticmethod
    def getCounter():
        return Funktor.functionCallCounter
    
@Funktor
def test():
    return 0

@Funktor 
def test2():
    return 1

print(Funktor.getCounter())
test()
print(Funktor.getCounter())
for _ in range(5):
    test2()
    
print(Funktor.getCounter())

    

