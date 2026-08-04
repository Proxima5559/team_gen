from pydantic import BaseModel, Field

class TeamGenerateRequest(BaseModel):
    club_name: str = Field(min_length=2, max_length=80)
    country: str = Field(min_length=2, max_length=80)
    league: str = Field(min_length=2, max_length=120)
    budget: int = Field(gt=0)
    formation: str = Field(default="4-3-3", min_length=3, max_length=20)
    playing_style: str = Field(default="balanced", min_length=2, max_length=50)