from models.group import Group
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
