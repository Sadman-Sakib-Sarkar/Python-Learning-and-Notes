from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass #null implementation

class TextBox(UIControl):
    def draw(self):
        print("TextBox")
    
class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(control): #here we are passing object as parameter
    control.draw()

ddl = DropDownList()
draw(ddl)

textbox = TextBox()
draw(textbox)

def drawtuple(controls): #here we are passing a list as parameter
    for control in controls:
        control.draw()

drawtuple([ddl, textbox])


#Poly = Many, Morphism = Form

