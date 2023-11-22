class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(4, 6)

print(point == other)
print(point > other)
print(point < other) #no need to implement for '<' as '>' is defined

#also we can perform arithmatic operation with magic methods
combined = point + other

print(combined.x)