from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

books = get_json(f"{BASE}/books")
print(books)

# run program: python3 client.py


new_book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
response = requests.post(f"{BASE}/books", json=new_book, timeout=5)
print(response.status_code, response.json())

get_json(f"{BASE}/books/99")
