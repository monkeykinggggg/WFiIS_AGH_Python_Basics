# Dziedziczenie, Iteratory
1. Proszę napisać iterator zwracający kolejny wyraz ciągu arytmetycznego dwoma sposobami i porównać ich wykorzystanie (2p)
2. Proszę utworzyć iterator zwracający liczbę pseudolosową generowaną wg wzoru X = (aX + c)%m, dla m = 2 , a = 44485709377909,
c = 0, x = 1. Korzystając z zaimplementowanego iteratora proszę sprawdzić ile punktów trzeba wylosować, aby obliczyć wartość całki z
zadaną dokładnością, np. 10 (stosujemy metodę Monte Carlo) (5p).  


Losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania. Wprowadzamy zmienną
pomocniczą t, którą modyfikować będziemy następująco:
jeżeli wylosowany punkt (xi, yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej, czyli spełnia nierówność: 0 < yi ≤
f(xi), wówczas zwiększamy zmienną t o jeden,
jeżeli wylosowany punkt (xi, yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej, czyli spełnia nierówność: 0 > yi ≥
f(xi), wówczas zmniejszamy zmienną t o jeden,
jeżeli wylosowany punkt (xi, yi) nie spełnia żadnego z powyższych warunków, wówczas pozostawiamy zmienną t bez zmian.
Całkę obliczamy jako P t/n  

3. Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: x =x -f(x )/f'(x ) z zadaną
dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x) , x=1.5 i eps=10 (pochodna - scipy.misc) (3p).