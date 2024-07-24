from pydantic import BaseModel


class TournamentDTO(BaseModel):
    name: str
    date: str
    is_completed: bool
