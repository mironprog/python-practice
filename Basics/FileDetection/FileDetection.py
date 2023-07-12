import os

path = "C:\\Users\\bmare\\OneDrive\\Desktop\\Miron\\code\\python-practice\\Basics\\FileDetection\\folder"

if os.path.exists(path):
    print("That location exists!")
    if(os.path.isfile(path)):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesnt exist!")