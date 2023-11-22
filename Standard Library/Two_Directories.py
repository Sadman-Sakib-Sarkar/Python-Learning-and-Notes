from pathlib import Path

path = Path("Standard Library/subfolder2") #here used relative path

## Some methods:
# path.exists()
# path.absolute()
# path.mkdir()
# path.rmdir()
# path.rename("subfolder3")

# path.iterdir()
for p in path.iterdir():
    print(p.name) #or print(p)

# Or we can use list of paths
paths = [p.name for p in path.iterdir()]
print("\n", paths)

# or
paths = [p for p in path.iterdir()]
print("\n", paths)

# if we want to print only directories
paths = [p for p in path.iterdir() if p.is_dir()]
print("\n", paths) 

# Limitations of iterdir(): can't search by pattern, it doesn't search recursively
# For searching we can use glob() method


#Search by pattern
py_files = [p for p in path.glob("*.py")]
print("\n", py_files)


#Search recursively
py_files = [p for p in path.rglob("*.py")]
print("\n", py_files)