import json
import os
from typing import List, Optional
from app.schemas.book import BookCreate, BookUpdate, BookRead

STORAGE_FILE = os.path.join(os.path.dirname(__file__), "../storage/books.json")

def _read_storage() -> List[dict]:
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def _write_storage(data: List[dict]):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def db_create_book(book_create: BookCreate) -> BookRead:
    data = _read_storage()
    
    ids_list: list[int] = []
    for record in data:
        ids_list.append(record["id"])
        
    if ids_list:
        max_id = max(ids_list)
    else:
        max_id = 0
    next_id = max_id + 1
    
    book_dict = book_create.dict()
    book_dict["id"] = next_id
    
    data.append(book_dict)
    _write_storage(data)
    
    return BookRead(**book_dict)
    

def db_list_books() -> List[BookRead]:
    data = _read_storage()
    book_list: List[BookRead] = []
    for book in data:
        book_list.append(BookRead(**book))
    return book_list

def db_get_book(book_id: int) -> Optional[BookRead]:
    data = _read_storage()
    for book in data:
        if book["id"] == book_id:
            return BookRead(**book)
    return None


def db_update_book(book_id: int, book_update: BookUpdate) -> BookRead:
    data = _read_storage()

    for record in data:
        if record["id"] == book_id:           
            update_fields = book_update.dict(exclude_unset=True)     
            record.update(update_fields)      
            _write_storage(data)        
            return BookRead(**record)

    raise ValueError(f"Book with id {book_id} not found")


def db_delete_book(book_id: int) -> bool:
    data = _read_storage()

    for record in data:
        if record["id"] == book_id:
            data.remove(record)
            _write_storage(data)
            return True
        
    return False
