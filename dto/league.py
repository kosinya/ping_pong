from pydantic import BaseModel


class LeagueBase(BaseModel):
    name: str
    n_groups: int = 4


class LeagueCreate(LeagueBase):
    tournament_id: int


class League(LeagueBase):
    id: int

    class Config:
        from_attributes = True
