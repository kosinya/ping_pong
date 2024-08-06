from sqlalchemy.orm import Session

from dto.department import DepartmentDTO
from models.department import Department


# Получить список всех отделений
def get_all_departments(db: Session):
    return db.query(Department).all()


# Получить отделение по id
def get_department_by_id(db: Session, department_id: int):
    return db.query(Department).filter_by(id=department_id).first()


# Создать новое отделение
def create_department(db: Session, department: DepartmentDTO):
    new_department = Department(name=department.name)
    try:
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
    except Exception as e:
        print(e)
        db.rollback()

    return new_department


# Изменить отделение по id
def update_department(db: Session, department_id: int, data: DepartmentDTO):
    dep = db.query(Department).filter_by(id=department_id).first()
    dep.name = data.name

    try:
        db.add(dep)
        db.commit()
        db.refresh(dep)
    except Exception as e:
        print(e)
        db.rollback()

    return dep


# Удалить отделение по id
def delete_department(db: Session, department_id: int):
    dep = db.query(Department).filter_by(id=department_id).delete()
    db.commit()
    db.refresh(dep)
    return dep
