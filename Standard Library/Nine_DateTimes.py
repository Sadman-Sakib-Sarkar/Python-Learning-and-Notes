# import datetime 
from datetime import datetime
import time

dt = datetime(2023, 11, 18) #year, month, date
current_dt = datetime.now()

print(dt)
print(current_dt)

## Parsing date time from any file or data
parsed_dt = datetime.strptime("1998/08/05", "%Y/%m/%d")
print(parsed_dt)

## from time.time() to datetime
time_to_dt = datetime.fromtimestamp(time.time())
print(time_to_dt)

## We can print date time using formatted text
print(f"{time_to_dt.year}/{time_to_dt.month}")

## We can format datetime using strftime (it's opposite to strptime)
print(parsed_dt.strftime("%Y/%m/%d"))

## We can compare
print(parsed_dt < current_dt)



