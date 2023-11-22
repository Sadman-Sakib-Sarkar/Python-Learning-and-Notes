import time #it gives us timestamp objects
import datetime #it gives us datetime objects (attributes like year, month and so on)

## Here we will see the time module
print(time.time())

def send_emails():
    for i in range(1000):
        pass

start = time.time()
send_emails()
end = time.time()

duration = end - start
print(duration) #we can find the total duration of sending the emails

#With this method we can find out the execution time of a block of code