from pydantic import BaseModel


class PlayerDTO(BaseModel):
    surname: str
    name: str
    patronymic: str
    department: str
    rating: int
