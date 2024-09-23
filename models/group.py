from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base
from models.player import Player
from models.league import League


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey(Player.player_id, ondelete='CASCADE'))
    score = Column(Integer)
    group_name = Column(String, index=True)
    league_id = Column(Integer, ForeignKey(League.league_id, ondelete='CASCADE'))
