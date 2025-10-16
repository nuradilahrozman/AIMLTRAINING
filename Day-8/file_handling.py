# import os
# file_path=r'D:\AIML\Day-8\files\sample.txt'
# file=open(file_path,'w')
# content=input('Enter text to write in file ')
# file.write(content)
# file.close()

# # this is without r. we add \
# import os
# file_path='D:\\AIML\\Day-8\\files\\sample.txt'
# file=open(file_path,'w')
# content=input('Enter text to write in file ')
# file.write(content)
# file.close()

# # to create the file in the Day-8 -> files -> new file
# import os
# file_path='D:\\AIML\\Day-8\\files'
# filename=input('Enter File Name to create : ')
# fullpath=os.path.join(file_path,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file ')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in file')
# file.close()

# # if want to add file in current directory (Day-8)
# import os
# file_path=os.getcwd
# filename=input('Enter File Name to create : ')
# fullpath=os.path.join(file_path,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file ')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in file')
# file.close()

