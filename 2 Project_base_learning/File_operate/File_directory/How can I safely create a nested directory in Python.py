'''
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
'''

import os

file_path = "/my/directory/filename.txt"
directory = os.path.dirname(file_path)

try:
    os.stat(directory)
except:
    os.mkdir(directory)

f = file(filename)