# JSON: JavaScript Object Notation (Popular way to format data in a human readable way)

import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]


data = json.dumps(movies)
print(data)

## Writing the json data on a file
Path("Standard Library/subfolder6/movies.json").write_text(data)


## Reading data from a json file
data = Path("Standard Library/subfolder6/movies.json").read_text() #it will give us string
movies = json.loads(data) #it will give us the list of movies
print(movies)
print(movies[0]["title"])
print(movies[1])