class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 2

    def eat(self):
        print("Eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__() #super() is used for accessing base classes method. It calls the constructor of the Animal class
        print("Mammal Constructor")
        self.weight = 5 #Method Overrided

    def walk(self):
        print("Walk")

m = Mammal()

m.walk()
print(m.weight)
print(m.age)