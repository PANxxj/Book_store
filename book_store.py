from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    published_date: date
    isbn: str
    price: float
    
books_db = []


@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")