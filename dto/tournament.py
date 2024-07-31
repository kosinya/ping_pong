from pydantic import BaseModel
from datetime import datetime


class TournamentDTO(BaseModel):
    name: str
    date: datetime
    is_completed: bool
