# import os
# file_path= r'C:\Users\Asus\Downloads\AIML\Day 8\ourfiles\sample.txt' 
# #file_path= 'C:\Users\Asus\Downloads\AIML\Day 8\\ourfiles\\sample.txt'
# file=open(file_path,'w')
# content=input('Enter text to write in file: ')
# file.write(content)
# file.close()

# import os
# # file_path= r'C:\Users\Asus\Downloads\AIML\Day 8\ourfiles\sample.txt'
# filepath= 'C:\\Users\\Asus\\Downloads\\AIML\Day 8\\ourfiles'
# filename=input('Enter file name to create file: \t')
# fullpath=os.path.join(filepath,filename)
# file=open(fullpath,'w')
# content=input('Enter text to write in file: ')
# file.write(content)
# print(f'file {filename} to craete at {fullpath} and content saved in file')
# file.close()


#3 option ---> to create new file under/in that folder
import os
# file_path= r'C:\Users\Asus\Downloads\AIML\Day 8\ourfiles\sample.txt'
filepath= os.getcwd()
filename=input('Enter file name to create file: \t')
fullpath=os.path.join(filepath,filename)
file=open(fullpath,'w')
content=input('Enter text to write in file: ')
file.write(content)
print(f'file {filename} to create at {fullpath} and content saved in file')
file.close()
