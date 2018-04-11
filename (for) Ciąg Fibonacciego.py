#Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba to suma dwóch poprzzednich, np:

fibonacciIterations=20
a1=0
a2=1
a3=a1+a2
for i in range(0,fibonacciIterations):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2
