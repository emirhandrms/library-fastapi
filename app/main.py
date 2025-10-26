from fastapi import FastAPI
from app.routers import books


app = FastAPI(title="Books API (Mock DB)",)

app.include_router(books.router)