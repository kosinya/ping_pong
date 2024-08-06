from pydantic import BaseModel


class PlayerDTO(BaseModel):
    surname: str
    name: str
    patronymic: str
    sex: int
    department_id: int
    rating: int
