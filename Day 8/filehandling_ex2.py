import os
# file_path= r'C:\Users\Asus\Downloads\AIML\Day 8\ourfiles\sample.txt'
filepath= os.getcwd()
filename=input('Enter file name to update file: \t')
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')
    content=input('Enter text to add in file: ')
    file.write(content)
    print(f'file content as follows')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')