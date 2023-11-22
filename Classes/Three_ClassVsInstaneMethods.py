class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Class Method
    @classmethod #decorator
    def zero(cls): #cls is conventionally used
        return cls(0, 0) #it is same as Point(0, 0)
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point.zero()
point.draw()