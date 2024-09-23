from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base
from models.tournament import Tournament


class League(Base):
    __tablename__ = 'leagues'

    league_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    n_groups = Column(Integer, nullable=False)
    tournament_id = Column(Integer, ForeignKey(Tournament.tournament_id, ondelete='CASCADE'))
    players = Column(String, nullable=False, default="")
