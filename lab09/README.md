# Modułu, Wyjątki

Proszę utworzyć moduł. Do modułu oraz do każdej funkcji w nim zdefiniowanej, proszę dodać łańcuch dokumentacyjny (1p), który proszę wyświetlić po imporcie modułu. Poszczególne wywołania funkcji oraz wyniki ich działania proszę logować (1p). W module proszę zdefiniować:

1. Funkcję sprawdzającą poprawność numeru karty kredytowej (2p)
Algorytm Luhna - cyfry w numerze karty indeksujemy od 15 (skrajna lewa) do 0 (skrajna prawa), indeksom parzystym nadajemy wagę jeden, a nieparzystym dwa, przy czym wartości na nieparzystych indeksach podwajamy, jeśli otrzymana liczba jest większa od 10 sumujemy jej cyfry. W numerze karty zastępujemy odpowiednio cyfry i przemnażamy je przez wagi, a następnie sumujemy. Jeżeli otrzymana wartość jest podzielna bez reszty przez 10 uznajemy numer karty za poprawny. Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, ma niepoprawną długość lub otrzymana suma kontrolna jest niepoprawna. Przykłady do testów : 924803, 1234567898765437, 1234567891234564, 1234567891234563

2. Funkcję sprawdzającą poprawność numeru PESEL (3p)
Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
Przykłady:
02070803628, 8 lipca 1902, kobieta
02270803624, 8 lipca 2002, kobieta
02270812350, 8 lipca 2002, mężczyzna

PESEL
cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
cyfry 3-4 to dwie cyfry miesiąca urodzenia
cyfry 5-6 to dwie cyfry dnia urodzenia
cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
cyfra 11 suma kontrolna

Do numeru miesiąca dodawane są następujące wartości w zależności od roku:
dla lat 1800 - 1899 - 80
dla lat 1900 - 1999 - 0
dla lat 2000 - 2099 - 20
dla lat 2100 - 2199 - 40
dla lat 2200 - 2299 - 60

Suma kontrolna: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić modulo 10.
Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.
Wyjątek zgłaszamy w przypadku kiedy parametr przekazany do funkcji nie składa się z samych cyfr, ma niepoprawną długość, cokolwiek innego się nie zgadza.

3. Funkcję zwracającą średni wiek osób, których daty urodzenia zapisane są w pliku daty.in. (3p)
Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  które tworzą poprawną datę - zgodność liczby dni w miesiącu, w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400.
