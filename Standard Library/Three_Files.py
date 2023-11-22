from pathlib import Path

path = Path("Standard Library/subfolder3/sales3.py")

print(path.exists())
# path.rename("newname.py")
# path.unlink() #for deleting the file
print("\n", path.stat())

## For see the creation time of the function
from time import ctime

print("\n", ctime(path.stat().st_ctime))


## For reading the data of the file
print("\n", path.read_text())


## For Copying
# import shutil

# source = Path("....")
# target = Path(".....")
# shutil.copy(source, target)