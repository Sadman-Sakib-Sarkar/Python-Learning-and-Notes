# Some times we get error while inputting some value or any illigal memory but
# we need to handle this situations in our application.

# Some Examples are as follows:

# numbers = [1, 2]
# print(numbers[3]) #here we will get index error

# age = int(input("Age: "))
# Here if we input any character we will get value error

# We need to handle these exceptions.


#ValueError:
print("Value Error: ")

try:
    age = int(input("Age: ")) 
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No Exception were thrown.")
    #The else block will work if no exception. It is not mendatory. Its like for-else.

print("Execution Continues.")


#Actual error message as variable
print("\nValue Error as variable: ")

try:
    age = int(input("Age: ")) 
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No Exception were thrown.")
    #The else block will work if no exception. It is not mendatory. Its like for-else.


#Zero Division Error
print("\nZero division error: ")

try:
    age = int(input("Age: ")) 
    xfactor = 10/age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero.")
else:
    print("No Exception were thrown.")


#Multiple Error in one exception
print("\nMultiple Error in one exception: ")

try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No Exception were thrown.")


# Finally Clause

# try:
#     file = open("Exception.py") #Opened file must be closed for other application to use it
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You don't enter a valid age.")
# else:
#     print("No Exception were thrown.")
# finally:
#     file.close() #This block always executes.



# # With Function (Alternative to finally clause)

# try:
#     with open("Exception.py") as file:
#         print("File Opened") #inside this block file can be manipulated and after this block it closes the file automatically.
#     age = int(input("Age: "))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You don't enter a valid age.")
# else:
#     print("No Exception were thrown.")

# This doesn't need to close as it closes automatically



# # With Function but working with multiple files (Alternative to finally clause)

# try:
#     with open("Exception.py") as file, open("Another.txt") as target:
#         print("File Opened") #After finishing the with block these two files will close automatically
# except (ValueError, ZeroDivisionError):
#     print("You don't enter a valid age.")
# else:
#     print("No Exception were thrown.")

# This doesn't need to close as it closes automatically


# Raising Exceptions:
print("\nRaising Exceptions: ")

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)