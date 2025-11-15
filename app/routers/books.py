from fastapi import APIRouter
from typing import List
from app.schemas.book import BookCreate, BookUpdate, BookRead
from app.logic.book import logic_create_book, logic_list_books, logic_get_book, logic_update_book, logic_delete_book

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BookRead],status_code=200,summary="List All Books")
async def list_books_endpoint():
    return logic_list_books()

@router.post("/", response_model=BookRead, status_code=201, summary="Create a New Book")
async def create_book_endpoint(book: BookCreate):
    return logic_create_book(book)

@router.get("/{book_id}", response_model=BookRead, status_code=200, summary="Get a Book by ID")
async def get_book_endpoint(book_id: int):
    return logic_get_book(book_id)

@router.put("/{book_id}", response_model=BookRead, status_code=200, summary="Update a Book by ID")
async def update_book_endpoint(book_id: int, book: BookUpdate):
    return logic_update_book(book_id, book)

@router.delete("/{book_id}", status_code=204, summary="Delete a Book by ID")
async def delete_book_endpoint(book_id: int):
    logic_delete_book(book_id)
    return
