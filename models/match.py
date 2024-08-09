from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    type = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    league_id = Column(Integer, ForeignKey('leagues.id'))
    winner_id = Column(Integer, ForeignKey('players.id'))

    player = relationship('Player', back_populates='match')
    group = relationship('Group', back_populates='match')
    league = relationship('League', back_populates='match')
