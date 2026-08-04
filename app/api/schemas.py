from pydantic import BaseModel, Field
from app.data.formation import FormationType


class TeamRequest(BaseModel):
    club_name: str | None = None
    country: str | None = None
    league: str | None = None
    budget: int | None = None
    formation: FormationType | None = None
    playing_style: str | None = None
    manager_name: str | None = None
    stadium_name: str | None = None
    min_strength: int | None = None
    max_strength: int | None = None
    seed: int | None = None