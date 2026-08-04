from pydantic import BaseModel

class Stadium(BaseModel):
    name: str
    city: str
    capacity: int