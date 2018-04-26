import os

webaddresses=[]

line=input('Enter web address like "www.python.org" or press ENTER to stop: ')

while line !='':
    webaddresses.append(line)
    line=input('Enter web address like "www.python.org" or press ENTER to stop: ')
print(webaddresses)

dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname,filename)
file=open(filepath,'w+')
for webaddress in webaddresses:
    file.write(webaddress+"\n")
file.close()

