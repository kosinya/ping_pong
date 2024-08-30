from database import Session
from models.playoff import Playoff
from dto import playoff


def create_playoff(db: Session, data: playoff.PlayoffCreate):
    new_playoff = Playoff(
        name=data.name,
        start_stage=data.start_stage,
        current_stage=data.current_stage,
        league_id = data.league_id
    )

    try:
        db.add(new_playoff)
        db.commit()
        db.refresh(new_playoff)
    except Exception as e:
        print(e)
        db.rollback()

    return new_playoff


def get_all_playoffs(db: Session, league_id: int):
    return db.query(Playoff).filter_by(league_id=league_id).all()
