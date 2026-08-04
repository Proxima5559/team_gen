from pydantic import BaseModel, Field
from typing import Literal

class Player(BaseModel):
    name: str
    age: int = Field(ge=17, le=40)
    kit_number: int = Field(ge=1, le=99)
    nationality: str
    position: str
    overall: int = Field(ge=40, le=99)
    potential: int = Field(ge=40, le=99)
    market_value: int = Field(ge=0)
    preferred_foot: Literal["Left", "Right", "Both"]

    height_cm: int = Field(ge=150, le=220)  
    weight_kg: int = Field(ge=50, le=120)   
    
    pace: int = Field(ge=20, le=99)
    shooting: int = Field(ge=20, le=99)
    passing: int = Field(ge=20, le=99)
    defending: int = Field(ge=20, le=99)
    physical: int = Field(ge=20, le=99)
    dribbling: int = Field(ge=20, le=99)
    goalkeeping: int = Field(ge=20, le=99)
    
    aggression: int = Field(ge=20, le=99)
    stamina: int = Field(ge=20, le=99)
    strength: int = Field(ge=20, le=99)
    jumping: int = Field(ge=20, le=99)
    heading: int = Field(ge=20, le=99)