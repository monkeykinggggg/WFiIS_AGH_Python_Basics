# Iteratory: map, zip, filter, reduce
1. Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję tak, aby uzupełnić poniższy kod:

``` python
import time
import sys

powt=1000
N=10000
(...)
print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
```
gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych jest N wartości.

Proszę wykonać testy (wszystko w ramach tych samych funkcji):
        dodawanie elementu
        dodawanie elementu podniesionego do kwadratu
        sumowanie elementów z wykorzystaniem pętli for
        sumowanie z wykorzystaniem funkcji sum
        konwersja obiektu map i generatora do listy

Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

2. Proszę wyznaczyć wartość liczby pi metodą Monte-Carlo korzystając z funkcji filter (2p)
Koło o promieniu 1 wpisujemy w kwadrat o boku 2 i umieszczamy ich środki w początku układu współrzędnych. Stosunek pól tych figur jest równy stosunkowi liczby trafień w ich obszar, przy losowaniu dużej liczby punktów wewnątrz kwadratu.

3. Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji wbudowanych sum i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności (wzory w pliku) (2p).

4. Proszę napisać funkcję myreduce przyjmującą dwa parametry (funkcję i sekwencję) oraz zwracającą liczbę. Funkcja przekazywana jako parametr będzie funkcją przyjmującą dwa parametry. Działanie funkcji proszę przetestować korzystając z wyrażenia lambda dla dodawania i mnożenia (2p)

5. Proszę znaleźć:
	- największą wartość w każdym wierszu macierzy (map),
	- największą wartość w każdej kolumnie macierzy (map+zip),
	- sumę dowolnej liczby macierzy (map+zip+lista składana)
Każde polecenie jedna linijka (2p)
