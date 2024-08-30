from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.league import League


class Playoff(Base):
    __tablename__ = 'playoffs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_stage = Column(String)
    current_stage = Column(String)
    league_id = Column(Integer, ForeignKey('leagues.id'))

    league = relationship("League")
