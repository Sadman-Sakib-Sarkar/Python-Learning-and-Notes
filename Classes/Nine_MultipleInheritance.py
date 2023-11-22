#Multilevel inheritance should be avoided. One or two level is good practice.
#If we do not use multiple inheritance properly it will also become bad.
#When there is same method in all the classes then it should handle carefully.

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    pass #pass class passes the interpreter without any issue.


m = Manager()
m.greet() #First it looks at Manager then it looks at Employee then it looks at Person