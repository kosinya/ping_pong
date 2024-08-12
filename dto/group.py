from pydantic import BaseModel


class GroupDTO(BaseModel):
    player_id: int
    score: int
    group_name: str
    league_id: int
    