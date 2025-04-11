import matplotlib.pyplot as plt

dict = {'q': 1, 'k': 2, 'v': 3, 'u': 6, 'g': 7, 'j': 8, 'd': 9, 'y': 10, 'h': 11, 'e': 11, 'r': 13, 'n': 13, 'm': 18, 'f': 24, 'c': 24, 'b': 25, 'l': 26, 'w': 33, 'o': 34, 'p': 35, 's': 36, 'a': 70, 'i': 70, 't': 107}
plt.bar(dict.keys(), dict.values())
plt.show()