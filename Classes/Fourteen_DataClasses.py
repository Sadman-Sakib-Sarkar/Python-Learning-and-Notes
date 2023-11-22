from collections import namedtuple

#If we need any class where we use only data and no methods then we can use namedtuple
Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=3, y=8)
p2 = Point(x=3, y=8)

print(p1 == p2) #We can easily compare two object without magic methods.
print(p1.x)
print(p1.y)

#this Point is immutable thats means we can't change value like this: p1.x = 10
#if we want to change then we need to create a new object

p1 = Point(x=10, y=8)
print(p1)