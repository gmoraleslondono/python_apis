from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

# get all movies
# movies = get_json(f"{BASE}/movies")
# print(movies)

# get one movie that doesn't exist
# get_json(f"{BASE}/movies/99")

# add one new movie
# new_movie = {
#     "title": "Titanic",
#     "director": "James Cameron",
#     "year": 1997
# }
# response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
# print(response.status_code, response.json())

# patch the year
request_body = {
    "year": "twentytwentyfive"
}
response = requests.patch(f"{BASE}/movies/4", json=request_body, timeout=5)
print(response.status_code, response.json())
