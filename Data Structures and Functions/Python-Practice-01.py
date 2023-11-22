import math
from collections import deque
from array import array

x = 3
print("Hey Sadman")
print("Hey Sadman")
print("check")
message = """
Hey this is a practice of message. 
Here in this format you can write anything in like a message box.
So thanks for stay with us.
"""

print(message)


print(len(message))
print(message[5:])
hello = "Hello"
this = "This is"
number = "Number"

full_name = f"{hello} {this}  {number} {34}"

print(full_name.upper())

print(message.title())

print(message.strip())

print(message.find("in l"))

print(message.replace("message", "MESSAGE"))

print("s" in message)
print("sadman" not in message)

print(103//4)
print(103/4)
print(10*4)
print(10**4)

print(math.ceil(2.1))
print(math.floor(2.9))

# x = input("Enter the value of x: ")
x = 25

print(type(x))

y = int(x) + 5

print(f"Value of x: {x} and value of y: {y}")

print(ord("b"))

# temp = input("Enter the temperature: ")
temp = 25

if int(temp) > 30:
    print("It's warm outside. \nDrink water.")

elif 20 < int(temp) < 30:
    print("It's a good weather outside. Enjoy the day!")

else:
    print("It's cold outside. \nWear warm cloth.")

# age = input("Enter age: ")
age = 25
msg = "Eligible" if int(age) >= 18 else "Not eligible"

print(msg)

# Logical Operator
high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# For Loop
for number in range(1, 10, 2):
    print("Printing", number, number*".")

# For...else
successful = False

for number in range(3):
    print("Attempt")

    if successful:
        break
else:
    print("Attempted 3 times but failed!")

# Nested Loop
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# String is iterable
for x in "Sadman":
    print(x)

# List is iterable
for x in [1, 4, 2, 5]:
    print(x)

# While Loop
number = 100

while number > 0:
    print(number)
    number //= 2

# Infinite Loop
command = "quit"  # use command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

# Exercise of Control Function
cnt = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        cnt += 1
print(f"We have {cnt} even numbers.")


# Function


def greet(first_name, last_name):
    print(f"Hey {first_name} {last_name}")
    print("This is inside the greet function.")


greet("Sadman", "Sakib")
greet("Fahima", "Momi")


# xargs
# (*)numbers is tuple here and it works as a collection of objects it is called tuple


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1, 2, 3, 4, 5))


# Dictionary: multiple keyword and value can be passed and it saves the values


def save_user(**user):  # here the user is a dictionary
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1, name="Sadman", age=20, country="Bangladesh")

# Debugging:
# F5 for start debugging and Shift+F5 to stop
# F9 is for break point add or remove
# F10 for line by line debugging
# F11 for entering function or line by line execution
# Shift + F11 for completing the functions task


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)


# value = input("Enter a value:")
# fizz_buzz(int(value))
fizz_buzz(15)

# List
names = ["Sakib", "Momi"]
matrix = [[0, 1], [2, 3]]
# filling list with same value
zeros = [0] * 10

print(matrix)
print(zeros)

# concate two list
combine = names + zeros
print(combine)

# list of range or serially increasing or decreasing numbers
numbers = list(range(20))
print(numbers)
print(numbers[::3])
print(numbers[::-1])
chars = list("Hello Sadman")
print(chars)
print(len(chars))

# List Unpacking
print("List unpacking: ")
numbers2 = [1, 2, 3]

# first = numbers2[0]
# second = numbers2[1]
# third = numbers2[2]

first, second, third = numbers2
print(first)

# Unpack few and others
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, third, *others = numbers3
print(second)
print(others)
print(type(second))
print(type(others))

# Unpack first last and others
numbers4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *others, last = numbers4
print(first, last)
print(others)

# iterate a list
print("Iterate a list: ")
letters = ['a', 'b', 'c', 'd', 'e']

for letter in letters:
    print(letter)

# enumerate returns a tuple with index
print("Enumarate returns a tuple with index: ")
for letter in enumerate(letters):
    print(letter)

# tuples also can be unpacked as list
items = (0, "a")
index, letter = items

for index, letter in enumerate(letters):
    print(index, letter)

# Removing or Adding item from list
# Adding
print("Adding: ")
letters.append("f")
print(letters)
letters.insert(0, "@")
print(letters)

# Removing
print("Popping/Removing: ")
letters.pop()
print(letters)
letters.pop(0)
print(letters)

# remove method removes an item with first occurance
print("Remove the first occurance: ")
letters.remove("d")
print(letters)

# del deletes any item or a range of items
print("Delete any item or range: ")
del letters[0:2]
print(letters)

# Delete all items from a list
print("Clear the list: ")
letters.clear()
print(letters)

# Finding Items
print("Item searching: ")
letters = ['a', 'b', 'c', 'd', 'e']
print(letters.count("d"))  # if count 0 then doesn't exist

if "d" in letters:
    print(letters.index("d"))  # returns the index of 1st occurence
    # if the item not in the list index() method returns error that's why if block is using

# Sorting List
print("Sorting: ")
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)  # sort changes the original list
print(numbers)
print(sorted(numbers))  # sorted makes a copy
print(numbers)
print(sorted(numbers, reverse=True))

# Sorting any list of tuple
print("Sorting list of tuple: ")
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1] #item[1] means it will sort based on the second element of item.


items.sort(key=sort_item)
print(items)

# Doing the same thing with lambda expression or function
# Syntax: (key = lambda parameters:expression)
print("Sorting with lambda: ")
items.sort(key=lambda item: item[1]) #item[1] means it will sort based on the second element of item.
print(items)


# Map Function
print("Map Function: ")
items = [
    ("Product1", 12),
    ("Product2", 15),
    ("Product3", 8),
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

# doing the same thing using map
print("Using map function: ")
x = map(lambda item: item[1], items)

for item in x:
    print(item)

# making list of the mapped item
prices = list(map(lambda item: item[1], items))
print(prices)

# Filter Function
print("Filter function: ")
x = filter(lambda item: item[1] >= 10, items)
for item in x:
    print(item)
# Or
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# List Comprehension similar as list map
# syntex: [expression for item in items]
print("List comprehensions: ")
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]  # both are similar

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]


# Zip Function
print("Zip function: ")
list1 = [2, 5, 9]
list2 = [20, 50, 90]

print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))


# Stack
print("Stack: ")
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
print(browsing_session[-1])
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    browsing_session[-1]
    print("disable")

# Queue and Deque
print("\nQueue/Deque: ")
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("Empty")

# tuple
print("\nTuple: ")

point = (1, 2)  # or 1, 2 but if only one then point = 1,
print(type(point))
print(point)
point = point + (3, 4)
print(point)
point = point*2
print(point)
point2 = tuple([9, 8, 7])
print(point2)
point3 = tuple("Hello World")
print(point3)
print(point3[0])
print(point3[0:5])
print(point3[::3])

point4 = (1, 2, 3)
x, y, z = point4
if 3 in point4:
    print("Exist!")

# Swaping
print("\nSwapping: ")
m = 23
n = 32

m, n = n, m #its actually unpacking a tuple (similar as m, n = (n, m))
print("m", m)
print("n", n)

#Array (Use array for large number of data and if performance drops)
print("\nArray: ")
numbers5 = array("i", [1, 2, 3, 4])
numbers5.append(5) #all methods of list can be applied
print(numbers5)

#Set (Unordered collection of unique items and we cannot duplicate + Objects are unordered)
print("\nSet: ")
numbers6 = [1, 1, 2, 3, 3, 2, 4, 5, 4, 5]
uniques = set(numbers6)
print(len(uniques))
print(uniques)
numbers7 = {2, 2, 3, 3, 4, 1, 1} #Curly braces are used for set
numbers7.remove(2)
numbers7.add(7)
print(numbers7)

#Union
print(uniques | numbers7)
#Intersection
print(uniques & numbers7)
#Difference
print(uniques - numbers7)
#Symmetric difference
print(uniques ^ numbers7)

#Dictionary
print("\nDictionary: ")
#point = {"x": 1, "y": 2}
point = dict(x=1, y=2) #similar to the previous
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)
#If not available
if "a" in point:
    print(point["a"])
print(point.get("a")) #OR
del point["x"]
print(point)
#iteration
for key in point:
    print(key, point[key])
#or we can get tuple
for x in point.items():
    print(x)
#we can unpack the tuple
for key, value in point.items():
    print(key, value)

#Dictionary Comprehensions
print("Dictionary Comprehensions: ")
values = []
for x in range(5):
    values.append(x*2)

values = [x*2 for x in range(5)] #same as the previous code
print(values)

#We can use this comprehensions to set and dictionary
#set
values2 = {x*2 for x in range(5)}
print(values2)

#dictionary
values3 = {}
for x in range(5):
    values3[x] = x*2

values3 = {x: x*2 for x in range(5)} #same as the upper code
print(values3)

#List, Set, Dictionary have comprehension but tuple don't have.
#values = (x*2 for x in range(10)) it creates a generator object which is itarable