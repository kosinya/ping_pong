from database import Base
from sqlalchemy import Column, Integer, String


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    patronymic = Column(String(30))
    sex = Column(Integer, nullable=False)
    department = Column(Integer, nullable=False)
    rating = Column(Integer, default=0, nullable=False)


