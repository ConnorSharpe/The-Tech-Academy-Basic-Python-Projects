# For this drill, you will need to write a script that will check a specific
# folder on the hard drive, verify whether those files end with a “.txt” file
# extension and if they do, print those qualifying file names and their
# corresponding modified time-stamps to the console.

# Requirements:
# Your script will need to use Python 3 and the OS module.
#import os

# Your script will need to use the listdir() method from the OS
# module to iterate through all files within a specific directory.
#os.listdir(path)

# Your script will need to use the path.join() method from the OS module
# to concatenate the file name to its file path, forming an absolute path.
#os.path.join(path,*paths)

# Your script will need to use the getmtime() method from the OS module to
# find the latest date that each text file has been created or modified.
#os.getmtime(path)

# Your script will need to print each file ending with a “.txt” file
# extension and its corresponding mtime to the console.

#if .txt file:
#    print(extension, os.getmtime(path))

import os

path = 'C:\\PyProjects\\'

print('These are the txt files in the directory:\n')

def checkTxt(dirName):
    listDir = os.listdir(path)
    for i in listDir:
        if i.endswith('.txt'):
            print(i, ':', os.path.getmtime(os.path.join(path,i)))

if __name__ == "__main__":
    checkTxt('C:\\PyProjects\\')
