def choinka(poziom):
    for i in range(1, poziom+1):
        print(" "*(poziom-i) + "*"*(2*i-1))
        print(" "*(poziom-i) + "O "*(i))
    print(" "*(poziom-1) + "*")
    print(" "*(poziom-2) + "***")


choinka(20)
