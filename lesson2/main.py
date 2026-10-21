from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Welcome to the Book API!"}

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

# validation with pydantic
class Book(BaseModel):
    title: str
    author: str
    year: int


# reuseable function to find a book by id
def find_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# serve all books
# serve books by author if author query parameter is provided
@app.get("/books")
def get_books(author: str | None = None):
    if author:
        return [book for book in books if book["author"].lower() == author.lower()]
    return books


# serve book by id
@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)
    return book


# create a new book
@app.post("/books", status_code=201)
def create_book(book: Book):
    new_id = max((b["id"] for b in books), default=0) + 1
    new_book = {"id": new_id, "title": book.title, "author": book.author, "year": book.year}
    books.append(new_book)
    return book


# update a book by id
@app.put("/books/{book_id}")
def replace_book(book_id: int, book: Book):
    existing_book = find_book(book_id)
    existing_book["title"] = book.title
    existing_book["author"] = book.author
    existing_book["year"] = book.year
    return existing_book


# delete a book by id
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    existing_book = find_book(book_id)
    books.remove(existing_book)

