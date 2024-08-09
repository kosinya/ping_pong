from pydantic import BaseModel
from typing import Literal


class PlayerDTO(BaseModel):
    surname: str
    name: str
    patronymic: str
    sex: Literal['муж.', 'жен.'] = 'муж.'
    department_id: int
    rating: int
