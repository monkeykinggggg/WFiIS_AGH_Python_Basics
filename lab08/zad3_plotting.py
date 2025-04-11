
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
                