# Write a python program to the contents of a directory using os module.
# search online for the function which does that.

import os

# specify the path of the directory you want to list
path = "/"

try:
    # get a list of files and directories in the given path
    contents = os.listdir(path)

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: Permission denied to access this directory.")
