from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
