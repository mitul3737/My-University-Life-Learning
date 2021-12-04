
import os
print(os.getcwd()) #shows current directory

#changing working directory to Filetest
os.chdir('E:\My-University-Life-Learning\Semester 1\Filetest')
#checking what are there in the directory
print(os.listdir())
#checking the current directory
print(os.getcwd())

#to make a directory
os.mkdir('New Directory')

#used to rename a directory
os.rename('New Directory','Updated Directory')


#remove a file
os.remove('<file_name>')

#remove a directory
os.rmdir('Updated directory')




