class Point:

    default_color = "red" #Class level attribute

    def __init__(self, x, y):
        self.x = x #instance attribute
        self.y = y #instance attribute
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
              
point = Point(4, 6)
point.z = 10 #instance attribute
point.draw()

#Each point has own attributes
another = Point(5, 7)
another.draw()

#Class attributes can be accessed/shared by all instances and class
print(point.default_color)
print(Point.default_color)
print(another.default_color)


#We can change class attribute but it will affect to all the instances
Point.default_color = "yellow"

print(point.default_color)
print(Point.default_color)
print(another.default_color)