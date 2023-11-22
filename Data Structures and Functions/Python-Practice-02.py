#Generator Object

from sys import getsizeof #it is to see the size of the generator object

print("\nGenerator object:")
values = (x*2 for x in range(5))
print(values)

for x in values:
    print(x)
    #Here values is not a list however it generates a new value in each iteration

values2 = (x*2 for x in range(100000))
print("Generator Object size in bytes: ", getsizeof(values2)) #result is in byte
#print(len(values2)) can't see length of a generator object

values3 = [x*2 for x in range(100000)]
print("List size in bytes: ", getsizeof(values3)) #result is in byte

#For big dataset we can use generator object
#We can just iterate but can't see total length of the generator object
#It generates a new value in each iteration

#Unpacking operator is: *
#There is another operator in javascript which is spread operator (...) which is exactly same as unpacking operator
print("\nUnpacking operator: ")
numbers = [1, 2, 3]
print(*numbers)

#We can unpack any iterable 
values4 = list(range(5))
print(values4)

values4 = [*range(5), *"Hello"]
print(values4)

#We can concatenate two list and add anything with unpack operator
first = [1, 2, 3]
second = [4, 5, 6]
allValues = [*first, "a", *second, *"Hey"]
print(allValues)

#If we want to unpack any dictionary then we need to use two *
one = {"x" : 4}
two = {"x" : 10, "y" : 5}
combined = {**one, **two, "z" : 2} #last value will be used. Here x = 10 will be used
print(combined)

print(*combined)
