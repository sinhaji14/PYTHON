import os
path = "C:\\Users\\yashs\\OneDrive\\Desktop\\New folder" #need double backslash for escape sequence for string

if os.path.exists(path): 
    print("that location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory ")
    else: 
        print("That location doesnt exist")