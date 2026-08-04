from typing import Optional
from pydantic import BaseModel

from app.models.manager import Manager
from app.models.player import Player
from app.models.stadium import Stadium
from app.data.formation import FormationType

class ClubIdentity(BaseModel):
    founded: int
    nickname: str
    club_name: str
    motto: str
    primary_color: str
    secondary_color: str
    mascot: str

class History(BaseModel):
    founded: int
    milestones: list[str]

class FanCulture(BaseModel):
    supporter_name: str
    atmosphere: str
    average_attendance: int
    reputation: str

class Jersey(BaseModel):
    home_primary: str
    home_secondary: str
    away_primary: str
    away_secondary: str
    third_primary: str
    third_secondary: str

class Team(BaseModel):
    # id: Optional[str] = None
    seed: Optional[int] = None
    name: str
    country: str
    league: str
    budget: int
    identity: ClubIdentity
    history: History
    fans: FanCulture
    formation: FormationType
    playing_style: str
    manager: Manager
    stadium: Stadium
    players: list[Player]
    jerseys: Jersey | None = None

    