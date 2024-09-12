from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.player import Player
from models.group import Group
from models.league import League
from models.playoff import Playoff


class Match(Base):
    __tablename__ = 'matches'

    match_id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.player_id'))
    player2_id = Column(Integer, ForeignKey('players.player_id'))
    type = Column(String, nullable=False)
    group_name = Column(String)
    playoff_id = Column(Integer, ForeignKey('playoffs.playoff_id'))
    league_id = Column(Integer, ForeignKey('leagues.league_id'))
    winner_id = Column(Integer, ForeignKey('players.player_id'))

    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])
    winner = relationship('Player', foreign_keys=[winner_id])
    league = relationship('League', foreign_keys=[league_id])
    playoff = relationship('Playoff', foreign_keys=[playoff_id])
