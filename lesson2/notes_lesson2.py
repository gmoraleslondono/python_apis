# Building APIs with FastAPI
# GET, POST, PUT, DELETE
# Return status code

# Install FastAPI
# python -m pip install "fastapi[standard]"

# Routes
# GET -> /books -> all books
# GET -> /books/{book_id} ->book by id
# POST -> /books -> create new book
# PUT -> /books/{book_id} -> update book
# DELETE -> /books/{book_id} -> delete book

# run the server (API) in a terminal
# cd to the project folder
# fastapi dev main.py

# api documentation
# http://127.0.0.1:8000/docs

#  validate with pydantic
# create an API class to set the data type

# Run the client in a separate terminal
# # cd to the project folder
# python3 client.py
