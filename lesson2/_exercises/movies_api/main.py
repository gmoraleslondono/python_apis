# Endpoints you build

# GET /movies
# GET /movies/{movie_id}
# POST /movies
# PUT /movies/{movie_id}
# DELETE /movies/{movie_id}

# 1 Start the server
# Create a folder movies_api with a file main.py. Create the app, add a list of four movies
# (id, title, director, year), and write the route GET /movies that returns the list. Start it
# with fastapi dev main.py and open /docs.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
  {
    "id": 1,
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010
  },
  {
    "id": 2,
    "title": "The Matrix",
    "director": "Lana Wachowski",
    "year": 1999
  },
  {
    "id": 3,
    "title": "Interstellar",
    "director": "Christopher Nolan",
    "year": 2014
  },
  {
    "id": 4,
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1972
  }
]

class Movie(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title : str | None = None
    director: str | None = None
    year: int | None = None



def find_movie(movie_id):
    for movie in movies:
            if movie["id"] == movie_id:
                return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# Get all movies
# @app.get("/movies")
# def get_movies():
#     return movies


# 2 Get one movie
# Add GET /movies/{movie_id}. If the id does not exist, answer with
# HTTPException(status_code=404). Test an id that exists, one that does not, and the
# text abc. Which status codes do you get?

# Get one movie
@app.get("/movies/{movie_id}")
def get_movie(movie_id:int):
    movie = find_movie(movie_id)
    return movie

# Test an id that exists
# http://127.0.0.1:8000/movies/1
# {
#   "id": 1,
#   "title": "Inception",
#   "director": "Christopher Nolan",
#   "year": 2010
# }
# status code 200

# Test an id that does not exist
# http://127.0.0.1:8000/movies/99
# {"detail":"Movie not found"}
# status code 404

# Test the text abc
# http://127.0.0.1:8000/movies/abc
# {"detail":[{"type":"int_parsing","loc":["path","movie_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc"}]}
# status code 422


# 3 Filter with a query parameter
# Let GET /movies take an optional director and an optional year. Without any of them
# you get all movies. Try /movies?director=scott and /movies?year=1999.

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    if director and year:
        return [movie for movie in movies if movie["director"].lower().strip() == director.lower().strip() and movie["year"] == year]
    elif director:
        return [movie for movie in movies if movie["director"].lower().strip() == director.lower().strip()]
    elif year:
        return [movie for movie in movies if movie["year"] == year]
    return movies

# Try /movies?director=Christopher+Nolan&year=2010
# [
#   {
#     "id": 1,
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "year": 2010
#   }
# ]

# Try /movies?director=Lana Wachowski
# [
#   {
#     "id": 2,
#     "title": "The Matrix",
#     "director": "Lana Wachowski",
#     "year": 1999
#   }
# ]


# Try /movies?year=1972
# [
#   {
#     "id": 4,
#     "title": "The Godfather",
#     "director": "Francis Ford Coppola",
#     "year": 1972
#   }
# ]

# Try /movies?director=scott
# [ ]


# 4 Add a movie
# Write a Movie class with Pydantic (title, director, year). Add POST /movies with
# status_code=201 that gives the new movie the next free id, adds it to the list and
# returns it. Test it in /docs. Then send a movie without a director and a year written as
# text. What do you get, and where does it tell you what is wrong?

@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((movie["id"] for movie in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

# movie without a director and a year written as
# text. What do you get, and where does it tell you what is wrong?
# Solution:
# 422	Error: Unprocessable Content
# a field is missing and a int_parsing error is raised.


# 5 Replace and remove
# You will now look up a movie by id three times, so move that code into a function
# find_movie(movie_id) that returns the movie or raises the 404. Use it in PUT
# /movies/{movie_id} (takes a full Movie) and in DELETE /movies/{movie_id} (answers
# 204). Delete the same movie twice. What happens the second time? Then save the file
# so that the server restarts, and check what happened to the movies you added.

@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing_movie = find_movie(movie_id)
    existing_movie["title"] = movie.title
    existing_movie["director"] = movie.director
    existing_movie["year"] = movie.year
    return existing_movie

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    existing_movie = find_movie(movie_id)
    movies.remove(existing_movie)

# Delete the same movie twice
# First time: 204 No Content
# Second time: 404 Not Found

# what happened to the movies you added after restart server?
# The movies added are gone because the list of movies is in memory and not persisted to a database file.


# 6 Call your own API from Python
# Copy api_client.py from yesterday into the folder. In a new file client.py, use
# get_json to get all movies and one movie that does not exist, and use requests.post
# to add a movie. Run the server in one terminal and client.py in another. Print the
# status code of the POST. Expected: the list of movies, The server said no: 404 for the
# missing movie, and 201 for the POST

# the list of movies
# [{'id': 1, 'title': 'Inception', 'director': 'Christopher Nolan', 'year': 2010}, {'id': 2, 'title': 'The Matrix', 'director': 'Lana Wachowski', 'year': 1999}, {'id': 3, 'title': 'Interstellar', 'director': 'Christopher Nolan', 'year': 2014}, {'id': 4, 'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972}]

# The server said no: 404 for the missing movie
# The server said no: 404

# 201 for the POST
# 201 {'id': 5, 'title': 'Titanic', 'director': 'James Cameron', 'year': 1997}


# PART 2 - PATCH
# 1 Write the model and the route
# Add the class MovieUpdate above, and a route PATCH /movies/{movie_id} that takes
# the id and a MovieUpdate. Use find_movie, then update the movie with the fields the
# client sent. Hint: movie.update(changes.model_dump(exclude_unset=True)). Return
# the updated movie

@app.patch("/movies/{movie_id}")
def movie_update(movie_id: int, changes: MovieUpdate):
    existing_movie = find_movie(movie_id)
    existing_movie.update(changes.model_dump(exclude_unset=True))
    return existing_movie

# 2 Test that only one field changes
# In /docs, send a body that only contains {"year": 2000}. Check with GET /movies/4
# that the title and the director are unchanged.
# 200 {'id': 4, 'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 2000}

# 3 Test the edges
# What happens with an empty body {}? And with a year written as text? And with an id
# that does not exist? Write down the status code for each.

# empty body {}
# 200 {'id': 4, 'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'year': 1972}
#  it returns the movie unchanged

# with a year written as text
# 422 {'detail': [{'type': 'int_parsing', 'loc': ['body', 'year'], 'msg': 'Input should be a valid integer, unable to parse string as an integer', 'input': 'twentytwentyfive'}]}

# id that does not exist
# 404 {'detail': 'Movie not found'}


# 4 Explain the difference
# Write two sentences, as a comment in your code, about when you would use PUT and
# when you would use PATCH.
# I would use put when need to update all the data from an entry (example: you need to change the year, director and name).
# Use patch when need to update only one attribute in the entry (example: only need to change the year).

