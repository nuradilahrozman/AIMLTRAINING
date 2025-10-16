#append/update
import os
filepath=os.getcwd()
filename=input('Enter File Name to update : ')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')
    content=input('Enter text to write in file ')
    file.write(content)
    print(f'File {filename} updated')
    file.close()
else:
    print(f'No such file {filename} exist')


