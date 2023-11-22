 #Here we will imoprt our movies.json file and upload to the SQLite database

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("Standard Library/subfolder6/movies.json").read_text())
# print(movies)


## Writing data on database:

# connection = sqlite3.connect("Standard Library/subfolder7/db.sqlite3") #it returns connection object and it should be closed

## Better approach using with:

# with sqlite3.connect("Standard Library/subfolder7/db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)" #These ? are placeholders

#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))

#     connection.commit()



## Reading data from database:

with sqlite3.connect("Standard Library/subfolder7/db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command) #it returns a cursor object which is iterable

    for row in cursor: #it takes the cursor at the end
        print(row)

    movies = cursor.fetchall() #it returns a list
    print(movies) #we can't see anything because the cursor is at the end now