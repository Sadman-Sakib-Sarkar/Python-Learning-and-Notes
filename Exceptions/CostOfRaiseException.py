from timeit import timeit #it determines the execution time

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    #print(error) #if use pass here then it will not execute the block.
    pass
"""

print("First Code: ", timeit(code1, number=10000)) #here number means how many time it will execute the code



code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None #None returns null value
    return 10/age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Second Code: ", timeit(code2, number=10000))


#Raise exception is not good when we need to execute for bigger scale as it is slower