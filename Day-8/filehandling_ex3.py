#write

import os
filepath=os.getcwd()
filename=input('Enter File Name to update : ')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'r')
    content=file.read()
    print('File content as follow ')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')