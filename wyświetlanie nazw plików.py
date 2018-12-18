
filename = 'H:\\UsersData\\lb24623\\pulpit\\wyniki.xls'
file = open(filename,'w')

from os import *
import glob

#print('wprowadz sciezke do podfolderów np.S:\\\\2015\\\\2015_WOZ\\\\') 
#sciezkauzytkownika=input()
#sciezkaprod=('%s' %(sciezkauzytkownika))

sciezkaprod='S:\\2007\\2007_ZPI\\'  #tutaj podajemy sciezke do podfolderu
plik='*\\*2007.*'                 #podajemy nazwe pliku, którego szukamy

chdir(sciezkaprod)
lista = glob.glob(sciezkaprod+plik)

for plik in lista:
    
    x=(plik.replace(sciezkaprod+'\\',' '))
    y=(x.replace('.xml',' ').replace('.doc',' ').replace('.xls',' ').replace('.XLS',' '))
    z=(y.replace('\\','                                        '))
    a=(z.replace('_','/').replace('TW/','').replace('CRD/CZ','CRD_CZ').replace('OZ/DSZ','OZ_DSZ').replace('OZ/DZZ','OZ_DZZ').replace('OZ/DWZ','OZ_DWZ').replace('mCO/WLA','mCO_WLA').replace('mCO/ZKM1A','mCO_ZKM1A'))
    b=(a[-27:])
    c=(b.replace(' ',''))
    print(c,file=file)
print('Udało się!!! Sprawdź plik "wyniki" na pulpicie')

    
file.close()
