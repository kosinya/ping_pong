from pydantic import BaseModel
from typing import Literal


class MatchBase(BaseModel):
    player1_id: int
    player2_id: int
    type: Literal['Групповой', '1/4', '1/2', 'Финал']
    group_name: str = None
    playoff_id: int = None
    league_id: int = None


class MatchCreate(MatchBase):
    pass


class Match(MatchBase):
    id: int
    winner_id: int = None

    class Config:
        from_attributes = True
