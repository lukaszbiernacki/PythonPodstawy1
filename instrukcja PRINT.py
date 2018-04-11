'''
Wyświetl napisy: TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV. Użyj jednego polecenia print
Wyświetl w/w teksty używając jako separatora znaku ";"
Korzystając z jednego polecenia print wyświetl napis (bez podtekstów!):
I like computers but better is TVP1 but better is TVP2 but better is TVN but better is Polsat but better is BBC but better is HBO but better is MTV 
Zadeklaruj zmienne ProgramName o wartości 'BBC', Item o wartości 'News'' i Time o wartości '18:00'. Nie używaj konkatenacji napisów (łączenia napisów). Użyj tylko polecenia print
Wyświetl napis (zwróć uwagę na kropkę na końcu!):
I like watching News at 18:00 on BBC .
Zmień napis tak, aby kropka była zaraz za  BBC. Nadal nie korzystamy z konkatenacji ale z pojedyńczego polecenia print.
'''

print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV')
print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=';')
print('I like computers ','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')
ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print('I like watching',Item,'at',Time,'on',ProgramName,'.')
print('I like watching ',Item,' at ',Time,' on ',ProgramName,'.', sep='')
