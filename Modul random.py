#biblioteka pozwalająca na pracę z funkcjami losowymi
import random 

# (random.randint) losuje liczbę całkowitą
print("One random number:",random.randint(1,100)) # 1 <= N <=100
print('\n')

#można tak:
print("choosing random number from a range",random.choice(range(1,100)))
print('\n')
#ale można krócej :)
print("Choosing random number from a range - easier",random.randrange(1,100))
print('\n')

#wymieszanie losowo listy, funkcja (random.shuffle)
list=['John','Anna','Peter','Sausen']
random.shuffle(list)
print("Reordered list:",list)
print('\n')

# funkcja (random.random() ) bez żadnych parametrów po prostu losuje liczbę float z zakresu od 0 do 1
print("Just a random float",random.random())
print('\n')
