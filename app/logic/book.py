from typing import List
from fastapi import HTTPException, status
from app.schemas.book import BookCreate, BookUpdate, BookRead
from app.db.book_crud import db_create_book, db_list_books, db_get_book, db_update_book, db_delete_book

def logic_create_book(book_create: BookCreate) -> BookRead:
    if book_create.published_year and book_create.published_year > 2100:
        raise HTTPException(status_code=400, detail="Published year seems too far in future, input less then 2100.")
    return db_create_book(book_create)

def logic_list_books() -> List[BookRead]:
    return db_list_books()

def logic_get_book(book_id: int) -> BookRead:
    book = db_get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def logic_update_book(book_id: int, book_update: BookUpdate) -> BookRead:
    book = db_update_book(book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def logic_delete_book(book_id: int):
    success = db_delete_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return
