import os

filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File dose not exist. Try again: ")
    filename = input("Enter filename to read: ")
webaddresses = []
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')
    
