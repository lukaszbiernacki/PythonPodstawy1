'''
Na konto została wpłacona kwota initialCapital w wysokości 20000.
Oprocentowanie na koncie to percent = 0.03.
Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat.
Po każdym roku oszczędzania zarobiona kwota jest dodawana do oszczędności i zarabia odsetki przez pozostały czas.

Zadeklaruj wymagane zmienne, a następnie stwórz pętlę,
która wyświetli informację o tym ile pieniędzy jest na koncie pod koniec roku,
kiedy odsetki się kapitalizują.
Dodaj na zakończenie informację o całkowitej kwocie zarobionej w banku.
'''

initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
