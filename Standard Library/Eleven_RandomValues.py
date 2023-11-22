import random

print(random.random()) #It generates random value from 0 to 1

print(random.randint(1, 10)) #It generates random integer from the given range

print(random.choice([1, 3, 5, 7, 9])) #It randomly chooses from the list

print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=2)) #It chooses k values from the list/range randomly

print(random.choices(range(10), k=2)) #It chooses k values from the list/range randomly

## With choices we can generate random passwords:
print(random.choices("abcd@#efgh*", k = 4)) # Randomly generates 4 character password
## We need to combine all these generated characters using "".join():
print("".join(random.choices("abcd@#efgh*", k = 4))) 
## Inside "" we can put anything which will appear as the separator:
print(",".join(random.choices("abcd@#efgh*", k = 4))) 


## Join method works on string or characters
list = ['3', '4', '5', '7', '8']
print(",".join(list))

## For using choices we can use string class
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

#Updated random password:
print("".join(random.choices(string.ascii_letters + string.digits, k = 4))) 

## We can shuffle an array using random.shuffle()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)