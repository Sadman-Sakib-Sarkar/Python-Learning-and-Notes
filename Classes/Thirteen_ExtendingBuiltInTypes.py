class Text(str):
    def duplicate(self):
        return self + self
    
text = Text("Python")
print(text.upper()) #string classes all methods can be accessed
print(text.duplicate())

class TrackableList(list):
    def append(self, object): #We can modify existing list methods also
        print("Append Called")
        super().append(object)

list = TrackableList()
list.append(5)
list.append(8)
print(list)