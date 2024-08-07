from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_connection
from dto.department import DepartmentDTO
from services import department


router = APIRouter()


# Создание нового отделения
@router.post('/', tags=['department'])
async def create_department(db: Session = Depends(get_connection), data: DepartmentDTO = None):
    return department.create_department(db, data)


# Получить список всех отделений
@router.get('/all', tags=['department'])
async def get_all_departments(db: Session = Depends(get_connection)):
    return department.get_all_departments(db)


@router.delete('/{id}', tags=['department'])
async def delete_department_by_id(id: str = None, db: Session = Depends(get_connection)):
    return department.delete_department(db, int(id))
