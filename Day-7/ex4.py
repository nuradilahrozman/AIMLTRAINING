# import os
# import inspect
# print('Current Directory',os.getcwd())
# print('Login Name: ', os.getlogin())

# function= inspect.getmembers(os,inspect.isbuiltin)

# print ('All function in os module')
# for n, func in function:
#     print(n)


#Create a folder inside current directory using python
# import os
# cdir=os.getcwd()
# folder_name=input('Enter Folder Name to create: ')
# folder_path=os.path.join(cdir, folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f"{folder_name} created at { folder_path}")

#Rename a folder
#os.rename(folder_name, "renamed_folder")
#write code to rename a folder
#you will take folderName from user
#if it is exist, yyou will ask new name and rename it
import os
cdir=os.getcwd()
folder_name=input('Enter the folder to rename :')
folder_path=os.path.join(cdir,folder_name)
if(os.path.exists(folder_path)):
    print('Folder Already Exist')
    os.makedirs(folder_name,exist_ok=True)
else:
    os.makedirs(folder_name,exist_ok=True)
    print(f"{folder_name} created at { folder_path}")

rename = input('Do you want to rename the folder? (yes/no): ').strip().lower()

if rename == 'yes':
    new_name = input('Enter new folder name: ')
    new_path = os.path.join(cdir, new_name)

    # Rename the folder
    os.rename(folder_path, new_path)
    print(f"Folder renamed to {new_name} at {new_path}")