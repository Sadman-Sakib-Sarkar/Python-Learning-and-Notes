
from abc import ABC, abstractmethod #abc: abstract base class. import ABC class and abstractmethod function

class InvalidOperationError(Exception):
    pass

class Stream(ABC): #it will be abstract class.
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass #abstract method remains empty.

class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")

class MemoryStream(Stream):
    def read(self): #implimenting abstract method is must.
        print("Reading data from a memory stream.")

    
# stream = Stream() #we cannot create object of abstract class.
#Also we can't create an object of any child class where implementation of abstract method is missing.
#Without implimenting the abstract method in child class acts as an abstract class.

stream = MemoryStream()
stream.read()