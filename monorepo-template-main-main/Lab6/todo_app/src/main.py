from fastapi import FastAPI, Body

app = FastAPI()
# Create a GET ReST API
@app.get("/api")
def first_api():
    return {"msg": "hello_world"}

# GET with path parameters
@app.get("/books/{path_para}")
def get_book_by_id(path_para: str):
    return {"msg": f"Getting book with ID {path_para}"}

# GET with query parameters
@app.get("/books/")
def get_books_by_title(title: str):
    return {"msg": f"Getting books with title containing: {title}"}

# GET with path parameters AND query parameters
@app.get("/books/{path_para}")
def get_books_by_id_and_title(path_para: str, title: str):
    return {"msg": f"Getting book with ID {path_para} and title containing: {title}"}

# POST
@app.post("/books/create_book")
def create_book(new_book=Body(...)):
    # Assuming new_book is a JSON payload
    return {"msg": "Book created successfully", "book_data": new_book}

# PUT
@app.put("/books/update_book/{book_id}")
def update_book(book_id: int, updated_book=Body(...)):
    # Assuming updated_book is a JSON payload
    return {"msg": f"Book with ID {book_id} updated successfully", "updated_data": updated_book}

# DELETE
@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    return {"msg": f"Book with ID {book_id} deleted successfully"}
