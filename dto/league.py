from pydantic import BaseModel


class LeagueBase(BaseModel):
    name: str
    n_groups: int
    tournament_id: int


class LeagueCreate(LeagueBase):
    pass


class League(LeagueBase):
    id: int

    class Config:
        from_attributes = True
