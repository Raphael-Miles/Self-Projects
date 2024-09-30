import os # Allows you to manipulate operating system 
import shutil # High level operations on files

path = input('Enter Path: ') # Takes the input for the directory path you want to organise
files = os.listdir(path) 

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:] # Removes dot as we only need extension name
    # Goes through each file in folder and splits the filename and extension of file
        
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file) # If extension directory already exists, gets moved into that directory
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file) # Makes a new directory if extension doesnt already exists and places file in there

