from pathlib import Path
from zipfile import ZipFile

## For zipping a whole folder with files

# with ZipFile("subfolder4.zip", "w") as zip: #'w' means write to the zip file
#     for path in Path("Standard Library/subfolder4").rglob("*.*"):
#         zip.write(path)

with ZipFile("Standard Library/subfolder4.zip") as zip: #zip needs to close thats why using with
    print(zip.namelist())
## Getting info of a file inside the zip
# info = zip.getinfo("Standard Library/subfolder4/sales1.py")
# print(info.file_size)
    info = zip.getinfo("Standard Library/subfolder4/sales1.py")
    print(info.file_size)
    print(info.compress_size) #here the file is very small thats why compress file and actual file has same size

    ## For extracting zipped file
    # zip.extractall("directory")
