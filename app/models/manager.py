from pydantic import BaseModel
from app.data.formation import FormationType

class Manager(BaseModel):
    name: str
    nationality: str
    formation: FormationType
    style: str