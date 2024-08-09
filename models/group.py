from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    score = Column(Integer)
    group_name = Column(String)
    league_id = Column(Integer, ForeignKey('leagues.id'))

    league = relationship('League', back_populates='group')
    player = relationship('Player', back_populates='group')
    match = relationship('Match', back_populates='group')