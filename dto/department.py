from pydantic import BaseModel


class DepartmentDTO(BaseModel):
    name: str
