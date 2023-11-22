# timedelta class gives duration
from datetime import datetime, timedelta

dt1 = datetime(1998, 8, 5)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("Days:", duration.days)
print("Seconds:", duration.seconds)
print("Total Seconds:", duration.total_seconds())


## We can add days with timedelta
dt2 = dt2 + timedelta(1) #We can use like: timedelta(days=1, seconds=2000)
duration = dt2 - dt1
print("\nOne Day Added: ", duration)
