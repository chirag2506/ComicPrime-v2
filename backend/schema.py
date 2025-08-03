from pydantic import BaseModel

class Comic(BaseModel):
    coverYear: int
    coverMonth: str
    issue: str
    releaseDate: str
    reprint: bool
    title: str
    toBeRead: bool
    url: str
    volume: int

class Volume(BaseModel):
    title: str
    toBeRead: bool
    url: str
    volume: int

class MonthRequest(BaseModel):
    coverYear: int
    coverMonth: str