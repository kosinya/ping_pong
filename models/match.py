from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.player import Player
from models.group import Group
from models.league import League


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    type = Column(String, nullable=False)
    group_name = Column(String)
    stage = Column(String)
    league_id = Column(Integer, ForeignKey('leagues.id'))
    winner_id = Column(Integer, ForeignKey('players.id'), default=None)

    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])
    winner = relationship('Player', foreign_keys=[winner_id])
