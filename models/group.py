from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.player import Player
from models.league import League


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'))
    score = Column(Integer)
    group_name = Column(String, index=True)
    league_id = Column(Integer, ForeignKey('leagues.league_id'))

    league = relationship('League')
    player = relationship('Player')
