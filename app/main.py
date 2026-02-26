from fastapi import FastAPI
from app.routers import books
from app.db.service import engine
from app.db.models import Base


app = FastAPI(title="Books API (Mock DB)",)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(books.router)