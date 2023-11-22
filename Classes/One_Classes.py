class Point:

    #Constractor
    def __init__(self, x, y): #this magic method id called constructor
        #self is a reference to the current point object
        self.x = x
        self.y = y


    def draw(self): #all methods in a class need atleast one parameter which is self
        print(f"Point ({self.x}, {self.y})")


point = Point(2, 6)
print(type(point))

print(isinstance(point, Point))
print(isinstance(point, int))

print(point.x)
point.draw()