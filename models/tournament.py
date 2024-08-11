from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from datetime import datetime


class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, nullable=False)
    date = Column(Date, nullable=False)
    is_completed = Column(Boolean, default=False)

    league = relationship('League', back_populates='tournament')
