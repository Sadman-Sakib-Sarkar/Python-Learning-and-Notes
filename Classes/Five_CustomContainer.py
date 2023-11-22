# #Custom Container Type

# class TagCloud:

# #Operation can be performed

# cloud = TagCloud()
# len(cloud)
# cloud["python"] = 20
# for tag in cloud:
#     print(tag)


class CloudTag:
    def __init__(self):
        self.__tags = {} #pressed f2 to rename and __ makes it private member.
    
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
        #.lower() is used for case sensitivity.

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags) #iter function provides an iterator object that provides one item at a time


cloud = CloudTag()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
cloud.add("Java")
print(cloud.__tags)

#value of the key from dictionary
print(cloud.__tags.get("python"))


#Some magic methods:
print(cloud["python"]) #__getitem__

cloud["C++"] = 5 #__setitem__
print(cloud.__tags) 

print(len(cloud)) #__len__

for item in cloud:
    print(cloud[item]) #__iter__

# print(cloud.__tags["python"]) #Can't access from outside.

# Accessing private members from outside
# It actually not unaccessable. It prevents unaccidental error.
# print(cloud.__dict__)
# it will return a method name then we can access.
# sample output {'_TagCloud__tags': {}}
# Then use:
# print(cloud._TagCloud__tags)
