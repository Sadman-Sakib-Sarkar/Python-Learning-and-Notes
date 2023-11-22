from pathlib import Path

## Examples for different OS
# Path("C:\\Program Files\\Microsoft") #windows
# Path(r"C:\Program Files\Microsoft") #windows but raw path
# Path("/usr/local/bin") #mac or linux
# Path() #path object that represent current folder
# Path("ecommerce/__init__.py") #relative path (we will use this)
# Path() / Path("ecommerce") / Path("__init__.py") #combining path objects together
# Path() / "ecommerce" / "__init__.py" #combining path object with strings
# Path.home() #home directory of the current user

path = Path("/home/triple_sa/Desktop/VSCode/Python Practice/Standard Library/subfolder1/sales.py") #here used absolute path

print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path = path.with_name("newfile.pdf") #it doesn't creates the file just represents the file name.
print(path)
#print(path.absolute()) #in this case its same
path = path.with_suffix(".txt") #its also just represents the name not creates any file.
print(path)
