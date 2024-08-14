from pydantic import BaseModel


class GroupBase(BaseModel):
    player_id: int
    score: int
    group_name: str
    league_id: int


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int

    class Config:
        from_attributes = True
    