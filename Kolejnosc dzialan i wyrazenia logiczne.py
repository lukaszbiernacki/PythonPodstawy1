'''
1. W tym zadaniu możesz się spodziewać ciekawego wyniku. (jeżeli chcesz sprawdzić jego działanie w innym roku niż 2017 to zmień liczbę 1017, np dla roku bieżącego 2019 należy użyć 1019):

>>> Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50. Całość pomnóż przez 20, a następnie dodaj 1017. Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.<<<

2. Kolejne działanie z tego samego cyklu:

>>>Pomyśl liczbe nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę. Powinno wyjść 5 - zawsze. <<<

3. Ile to jest - najpierw policz sam, a potem sprawdź rozwiązanie pythona

2+2*2 = ?

7+7/7+7*7-7 = ?

4. Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność co najmniej 80% i średnią >= 3.0 lub zaliczyłeś pracę semestralną. Zbuduj wyrażenie w Python które stwierdzi czy student, który ma obecność 0.85, średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.

5. Wykładowca zmienił zdanie. Aby zaliczyć semest trzeba: mieć obecność co najmniej 80%, średnią >=3.0 i zaliczoną pracę. Czy teraz student zda?

6. Zmieniamy dane studenta. Teraz ma obecność 40%. średnią 2.5 ale zaliczył pracę semestralną. Sprawdź wg którego z kryterów student zaliczy semestr.
'''

'''
Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50.
Całość pomnóż przez 20, a następnie dodaj 1017. Odejmij od tego swój rok urodzenia.
Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.
'''
shoesize = 45
number = (shoesize*5 +50)*20+1017 -1973
print('shoe size is:',number //100)
print('birth date is:',number %100)
'''
Pomyśl liczbe nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę.
Powinno wyjść 5 - zawsze.
'''
x=107
print('this should be 5:',(x*2+10)/2-x)
print('2+2*2=',2+2*2)
print('7+7/7+7*7-7',7+7/7+7*7-7)
presence = 0.85
note =3.5
finalWorkOK = False
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
presence = 0.4
note =2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
