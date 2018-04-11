#Ciąg Fibonacciego

fibonacciIterations=20
a1=0
a2=1
a3=a1+a2
for i in range(0,fibonacciIterations):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2
