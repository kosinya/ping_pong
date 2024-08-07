from pydantic import BaseModel


class PLayerDTO(BaseModel):
    name: str
    n_groups: int
    tournament_id: int
