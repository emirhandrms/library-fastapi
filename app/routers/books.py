from fastapi import APIRouter
from typing import List
from app.schemas.book import BookCreate, BookUpdate, BookRead
from app.services.book_service import service_create_book, service_list_books, service_get_book, service_update_book, service_delete_book

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BookRead],status_code=200,summary="List All Books")
async def list_books_endpoint():
    return service_list_books()

@router.post("/", response_model=BookRead, status_code=201, summary="Create a New Book")
async def create_book_endpoint(book: BookCreate):
    return service_create_book(book)

@router.get("/{book_id}", response_model=BookRead, status_code=200, summary="Get a Book by ID")
async def get_book_endpoint(book_id: int):
    return service_get_book(book_id)

@router.put("/{book_id}", response_model=BookRead, status_code=200, summary="Update a Book by ID")
async def update_book_endpoint(book_id: int, book: BookUpdate):
    return service_update_book(book_id, book)

@router.delete("/{book_id}", status_code=204, summary="Delete a Book by ID")
async def delete_book_endpoint(book_id: int):
    service_delete_book(book_id)
    return
