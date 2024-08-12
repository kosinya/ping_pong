from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.tournament import Tournament


class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    n_groups = Column(Integer, nullable=False)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))

    tournament = relationship('Tournament')
