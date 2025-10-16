# import os

# print ('Current directory: ', os.getcwd())


# functions= inspect.getmembers(os, inspect.isbuiltin)

# print('All function in math module')
# for n, func in functions:
#     print(n)

#create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folder_name=input('Enter folder name to create: \t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder already exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

#rename a folder
#exercises
# os.rename(folder_name, "renamed_folder")
#write code to rename a folder
#you will take folderName from user
#if it is exist, you will ask new name and rename it

# rename_folder.py
# Rename a folder inside the current directory using Python

# import os
# cdir = os.getcwd()

# # Take folder name from user
# folder_name = input("Enter the folder name to rename: ").strip()
# old_path = os.path.join(cdir, folder_name)

# # Check if the folder exists
# if os.path.exists(old_path) and os.path.isdir(old_path):
#     new_name = input("Enter the new folder name: ").strip()
#     new_path = os.path.join(cdir, new_name)

#     # Check if new name already exists
#     if os.path.exists(new_path):
#         print(f"A folder named '{new_name}' already exists.")
#     else:
#         os.rename(old_path, new_path)
#         print(f" Folder renamed from '{folder_name}' to '{new_name}'.")
# else:
#     print(f" Folder '{folder_name}' does not exist in {cdir}.")

import calc
print('Average of 10,20 is')
