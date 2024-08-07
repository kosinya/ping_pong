from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    player = relationship("Player", back_populates="department")
