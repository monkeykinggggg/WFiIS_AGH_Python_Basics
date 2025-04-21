task_index=1
def zadanie(i):
    return f' ZAD {i} '

########### ZAD 1 ############
print()
space = '#'*10
print(space+zadanie(task_index)+space)

import abc

class Calka(abc.ABC):
    def __init__(self,start,stop,n,func):
        if not isinstance(start, [float,int]) or not isinstance(stop, [float,int]) or start>stop:
            raise ValueError('Granica calkowania powinna byc liczbą, pierwsza powinna być mniejsza od drugiej')
        if not isinstance(n, int) or n<=0:
            raise ValueError('n powinno byc dodatnim int-em')
        if not isinstance(func, function):
            raise ValueError('ostatnim argumentem powinna być referencja do funkcji')
        self.xp = start
        self.xk = stop
        self.n = n
        self.func = func
        
    @abc.abstractmethod
    def evaluate(self):
        '''abstract method evaluating integral'''
        
class Simpson(Calka):
    def __init__(self,start,stop,n,func):
        super().__init__(start, stop, n, func)
        
    def evaluate(self):
        h = (self.xk-self.xp)/(self.n*2)
        s = h/2*(self.func(self.xp)+4*sum(self.func(x) for x in range(self.xp,)))