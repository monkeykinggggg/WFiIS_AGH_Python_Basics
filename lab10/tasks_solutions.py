task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import random
import matplotlib.pyplot as plt

class IFS():
    def __init__(self,sets, probability=None):
        self.point = (0,0)
        self.sets = sets
        self.probability = probability
        self.function = []
        self.function.append(self.point)
    
        
    def przeksztalcenie(self, iters = 100):
        for it in range(iters):
            # losujemy inna szóstkę z zestawu współczynników
            coeffitients = random.choices(self.sets, weights = self.probability, k=1)[0]
            self.point = (coeffitients[0]*self.point[0] + coeffitients[1]*self.point[1] + coeffitients[2], coeffitients[3]*self.point[0] + coeffitients[4]*self.point[1] + coeffitients[5])
            self.function.append(self.point)
    
    def narysuj_funkcje(self,filename):
        xs = [point[0]for point in self.function]
        ys = [point[1]for point in self.function]
        plt.figure()
        plt.plot(xs,ys,".", markersize=1)
        plt.savefig(filename)
            

test1 = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
test1.przeksztalcenie(50000)
test1.narysuj_funkcje('test1.png')


test2 = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))
test2.przeksztalcenie(50000)
test2.narysuj_funkcje('test2.png')

test3 = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)),  (0.8, 0.2))
test3.przeksztalcenie(50000)
test3.narysuj_funkcje('test3.png')

########### ZAD 2 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import math
class Wektor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        if isinstance(other, Wektor3D):
            return  Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError(f'Niepoprawny typ danych do dodania: {type(other)}')
        
    __radd__ = __add__
    
    def __iadd__(self, other):
        if isinstance(other, Wektor3D):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        else:
            raise ValueError(f'Niepoprawny typ danych do dodania: {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Wektor3D):
            return  Wektor3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError(f'Niepoprawny typ danych do odejmowania: {type(other)}')
            
    __rsub__ = __sub__
    
    def __isub__(self, other):
        if isinstance(other, Wektor3D):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        else:
            raise ValueError(f'Niepoprawny typ danych do dodania: {type(other)}')

    def __mul__(self,number):
        if isinstance(number, (int,float)):
            return Wektor3D(self.x*number, self.y*number, self.z*number)
        else:
            raise ValueError(f'Niepoprawny typ danych do mnożenia: {type(number)}')
            
    __rmul__ = __mul__
    
    def __imul__(self,number):
        if isinstance(number, (int,float)):
            self.x *= number
            self.y *= number
            self.z *= number
            return self
        else:
            raise ValueError(f'Niepoprawny typ danych do mnożenia: {type(number)}')
        
    def __str__(self):
        return f'[ {self.x}, {self.y}, {self.z} ]'
    
    def length(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def skalar_multiplication(self, other):
        if isinstance(other,Wektor3D):
            return self.x*other.x + self.y*other.y + self.z*other.z
        else:
            raise ValueError(f'Niepoprawny typ danych do mnożenia skalarnego: {type(other)}')
        
    def vector_multiplication(self, other):
        if isinstance(other, Wektor3D):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Wektor3D(x,y,z)
        else:
            raise ValueError(f'Niepoprawny typ danych do mnożenia wektorowego: {type(other)}')
        
    def mixed_multiplication(self, other):
        return self.skalar_multiplication(self.vector_multiplication(other))
    
v1 = Wektor3D(1,2,3)
v2 = Wektor3D(4,5,6)
v3 = Wektor3D(7,9,9)
print(v1+v2)
print(v1*5)
print(5*v1)
print(v1.length())
print(v1.skalar_multiplication(v2))
print(v1.vector_multiplication(v2))
print(v1.mixed_multiplication(v3))


########### ZAD 3 ############
task_index+=1
print()
space = '#'*10
print(space+zadanie(task_index)+space)
B = Wektor3D(1,2,3)
S = Wektor3D(4,5,6)
v = Wektor3D(7,9,9)
E = Wektor3D(1,1,1)
q = 1

def induction(B,S):
    if isinstance(B, Wektor3D) and isinstance(S, Wektor3D):
        return B.skalar_multiplication(S)
    else:
        raise ValueError(f'Argumenty muszą być wektorwami typu Wektor3D')
def Lorentz_force(E,q,B,v):
    if isinstance(E, Wektor3D) and isinstance(B, Wektor3D) and isinstance(v, Wektor3D):
        return (E + v.vector_multiplication(B))*q
    else:
        raise ValueError(f'Argumenty E,B,v muszą być wektorami typu Wektor3D')
    
def Lorentz_work(q,E,v):
    if isinstance(E, Wektor3D) and isinstance(v, Wektor3D):
        return E.skalar_multiplication(v) *q
    else:
        raise ValueError(f'Argumenty E,v muszą być wektorami typu Wektor3D') 
       
print(f'Strumień indukcji magnetycznej =  {induction(B,S)}')
print(f'Siła Lorentza = {Lorentz_force(E,q,B,v)}')
print(f'Praca siły Lorentza = {Lorentz_work(q,E,v)}')
