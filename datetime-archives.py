"""
This script creates an empty file with date and time (2017-09-16-16-55) information.
1 - Define the extension.
2 - Creates the file based on time and date.
github.com/aliceturino
"""
import datetime

extension = input("Type the extension that you want in the file (.txt by default):\n")
filename =  datetime.datetime.now()

def extension_check(): #checking if the variable extension has a "." at the start
    global extension
    try:
        if extension[0] == ".":
            return "Ready to go!"
        else:
            extension = ".txt" #defining default extension
            return "Using default extension .txt"
    except IndexError: # avoiding string index out of range and using the default extension instead
        extension = ".txt"
        return "Blank input... Using default extension .txt"

def create_file():
    #strftime.org/
    with open(filename.strftime("%Y-%m-%d-%H-%M")+ extension, "w") as file:
        file.write("") #writing empty string

extension_check()
create_file()
