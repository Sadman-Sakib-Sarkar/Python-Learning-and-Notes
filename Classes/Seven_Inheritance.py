class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

class Mammal(Animal): #Inherit from Animal Class
    def walk(self):
        print("Walk")

class Fish(Animal): #Inherit from Animal Class
    def swim(self):
        print("Swim")

#Animal: Parent class or Base class
#Mammal, Fish: Child class or Sub class

m = Mammal()
m.eat()
print(m.age)

print(isinstance(m, Mammal))
print(isinstance(m, Animal)) 
print(isinstance(m, object)) #All classes are inherited from the base object class in python

o = object()
#we can see all the magic methods by typing 'o.'

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))
