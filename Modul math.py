f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math

# funkcja (math.ceil) zwraca dla wskazanego argumentu najmniejszą liczbę całkowitą, która jest większa od przekazanego argumentu
print(math.ceil(f_smaller),math.ceil(f_bigger)) 
print('\n')

# funkcja *math.floor) zwraca największą liczbę która jest mniejsza od podanego argumentu
print(math.floor(f_smaller),math.floor(f_bigger))
print('\n')

print(math.ceil(-f_smaller),math.ceil(-f_bigger))
print('\n')

print(math.floor(-f_smaller),math.floor(-f_bigger))
print('\n')

# funkcja (pow) mówi do jakiej potęgi chcesz podnieść liczbe
print(pow(2,8),pow(9,0.5))
print('\n')

# (math.sqrt) pierwiastek kwadratowy
print(math.sqrt(16))
print('\n')

# stała (math.pi) i (math.e)
print(math.pi, math.e)
print('\n')

# sinus , cosinus
print(math.sin(math.pi/2),math.cos(math.pi/4))
print('\n')
