# duży lotek + nagroda

import random

def ustawienia():
    # Funkcja pobiera ilość losowanych liczb, maksymalną losowaną wartość
    # oraz ilość prób. Pozwala określić stopień trudności gry.
    while True:
        try:
            ile = int(input("Podaj ilość typowanych liczb: "))
            maks = int(input("Podaj maksymalną losową liczbę: "))
            if ile > maks:
                print("Błędne dane!")
                continue
            ilelos = int(input("Ile losowań: "))
            return (ile, maks, ilelos)
        except ValueError:
            print("Błędne dane!")
            continue

def wylosowane(ile, maks):
    # Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks
    wylosowane = []
    i=0
    while i < ile:
        liczba = random.randint(1,maks)
        if wylosowane.count(liczba) == 0:
            wylosowane.append(liczba)
            i = i+1
    return wylosowane
        


def pobierztypy(ile, maks):    
    # Funkcja pobiera od użytkownika jego typy wylosowanych liczb
    print("Wytypuj %s z %s liczb: " %(ile, maks))
    typy = []
    i=0
    while i < ile:
        try:
            typ = int(input("Podaj liczbę %s: " %(i+1)))
        except ValueError:
            print("Błędne dane!")
            continue
        
        if typy.count(typ) == 0 and maks >= typ > 0:
            typy.append(typ)
            i = i+1
    return typy
    
    

