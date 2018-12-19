
from Duży_Lotek_Moduł import ustawienia, wylosowane, pobierztypy
from choinka_Modul import choinka

def main(args):
    # ustawienia gry
    ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby_wylosowane = wylosowane(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        trafione = set(liczby_wylosowane) & set(typy)
        if len(trafione) == ileliczb:
            print("GRATULACJE !!!")
            choinka(13)
            break
        
        elif trafione:
            print("Ilość trafień: %s" % len(trafione))
            print("Trafione liczby: ", trafione)
            
        else:
            print("Brak trafień. Spróbuj jeszcze raz!") 
        print("X"*40)

    print("\nWylosowane liczby to: ",liczby_wylosowane)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
