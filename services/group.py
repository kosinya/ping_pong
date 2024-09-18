from models.group import Group
from models.player import Player
from dto import group
from database import Session


def add_player_to_group(db: Session, data: group.GroupCreate, league_id: int):
    new = Group(
        player_id=data.player_id,
        score=data.score,
        group_name=data.group_name,
        league_id=league_id
    )

    try:
        db.add(new)
        db.commit()
        db.refresh(new)
    except Exception as e:
        print(e)
        db.rollback()

    return new


def get_all_groups(db: Session, l_id: int):
    return db.query(Group).filter(Group.league_id == l_id).order_by(Group.group_name.asc(), Group.score.desc()).all()
