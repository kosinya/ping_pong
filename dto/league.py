from pydantic import BaseModel


class LeagueDTO(BaseModel):
    name: str
    n_groups: int
    tournament_id: int
