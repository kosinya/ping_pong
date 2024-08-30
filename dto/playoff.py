from pydantic import BaseModel
from typing import Literal


class PlayoffBase(BaseModel):
    name: Literal['Gold', 'Silver', 'Bronze'] = 'Gold'
    start_stage: Literal['1/4', '1/2', 'Финал'] = '1/8'
    current_stage: Literal['1/4', '1/2', 'Финал'] = '1/8'
    league_id: int


class PlayoffCreate(PlayoffBase):
    ...


class PlayoffUpdate(PlayoffBase):
    id: int

    class Config:
        from_attributes = True
