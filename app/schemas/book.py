from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., example="Çalınan Dikkat - Neden Odaklanamıyoruz?")
    author: str = Field(..., example="Johann Hari")
    description: Optional[str] = Field(None, example="Johann Hari'nin Çalınan Dikkat eseri, modern insanın odaklanma yetisini neden kaybettiğini kişisel bir kusurdan öte, sistemli bir saldırı olarak ortaya koyuyor. Artan hız, uyku sorunları ve bizi ekrana hapsetmek için tasarlanmış teknolojiler, yazarın işaret ettiği temel nedenlerden sadece birkaçı.")
    published_year: Optional[int] = Field(None, ge=0, example=2008)


class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = Field(None, ge=0)

class BookDelete(BookBase):
    id: int