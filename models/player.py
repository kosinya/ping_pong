from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.department import Department


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    patronymic = Column(String(30))
    sex = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    rating = Column(Integer, default=0, nullable=False)

    department = relationship("Department")
