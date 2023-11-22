import numpy as np #np is an alias

array = np.array([1, 2, 3, 4, 5])
print(array)
print("\n", type(array))

#2d array:
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n", array2d)

print("\n", array2d.shape) # Shape gives us the dimension of the matrix

## initializer with zeros or other values:
array3 = np.zeros((3, 4), dtype=int) # a 3 by 4 matrix with all values 0 (bydefault floating point)
print("\n", array3)

array4 = np.ones((3,4), dtype=int) #ones method fills with 1
print("\n", array4)

array5 = np.full((3,4), 5, dtype=int) #full method takes a value to fill the matrix (here 5)
print("\n", array5)

array6 = np.random.random((3,4)) # we can fill the matrix with random values
print("\n", array6)

## Accessing array elements:
print("\n", array6[0, 0])


## We can compare with any value easily:
print("\n", array6 > 0.25)
print("\n", array6[array6 > 0.2]) #using boolean expression (it returns only the values greater than 0.2)

## Sum of array:
print("\n", np.sum(array6))

## Floor:
print("\n", np.floor(array6))

## Ceil:
print("\n", np.ceil(array6))

## Round:
print("\n", np.round(array6))


## Arithmatic operation on arrays:
first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print("\n", first + second) #add, sub, div, mul all operation supported
print("\n", first + 2)

## We can change the dimension of an array like from inch to cm:
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print("\n", dimensions_cm)

