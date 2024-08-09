from pydantic import BaseModel
from typing import Literal


class Match(BaseModel):
    player1_id: int
    player2_id: int
    type: Literal['Групповой', '1/32', '1/16', '1/8', '1/4', '1/2', 'Финал']
    group_id: int
    league_id: int
    winner_id: int
